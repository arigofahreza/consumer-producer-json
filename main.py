import json
from argparse import ArgumentParser

from confluent_kafka import Consumer, OFFSET_BEGINNING, Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField

from schema import schema_repo
from helpers.converters import to_dict, DictToObj

parser = ArgumentParser()
parser.add_argument('--reset', action='store_true')
parser.add_argument('--offset', default=-1, type=int)
args = parser.parse_args()

if __name__ == '__main__':

    def reset_offset(consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            consumer.assign(partitions)


    schema_registry_conf = {'url': 'http://localhost:8081'}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    string_serializer = StringSerializer('utf_8')

    bootstrap_servers = 'localhost:9092'

    producer = Producer({'bootstrap.servers': bootstrap_servers})

    c = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'consume-json13',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe(['my_topic1', 'mytopic_2'], on_assign=reset_offset)

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            pass
        else:
            decoded_message = msg.value().decode()
            json_data = json.loads(decoded_message)
            table_name = msg.topic().replace('.', '_')
            schema_function = getattr(schema_repo, table_name)
            schema_string = schema_function()
            json_serializer = JSONSerializer(schema_string, schema_registry_client, to_dict)
            message_object = DictToObj(json_data)
            split_topic = msg.topic().split('.')
            topic_producer = f'{split_topic[0]}_SCHEMA.{split_topic[1]}'
            producer.produce(topic=topic_producer,
                             key=msg.key(),
                             value=json_serializer(message_object, SerializationContext(topic_producer, MessageField.VALUE)))
            print(json_data)

    c.close()
