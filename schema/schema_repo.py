def FL_CDC_SHOPPING():
    return """{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "my_topic1",
  "type": "object",
  "properties": {
    "magic": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "headers": {
      "type": "null"
    },
    "messageSchemaId": {
      "type": "null"
    },
    "messageSchema": {
      "type": "null"
    },
    "message": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "ORDER_ID": {
              "type": "integer"
            },
            "PRODUCT_ID": {
              "type": "integer"
            },
            "QUANTITY": {
              "type": "integer"
            },
            "PRICE": {
              "type": "string"
            },
            "CUSTOMER_ID": {
              "type": "integer"
            },
            "ORDER_DATE": {
              "type": "string"
            }
          }
        },
        "beforeData": {
          "type": "null"
        },
        "headers": {
          "type": "object",
          "properties": {
            "operation": {
              "type": "string"
            },
            "changeSequence": {
              "type": "string"
            },
            "timestamp": {
              "type": "string"
            },
            "streamPosition": {
              "type": "string"
            },
            "transactionId": {
              "type": "string"
            },
            "changeMask": {
              "type": "null"
            },
            "columnMask": {
              "type": "null"
            },
            "transactionEventCounter": {
              "type": "null"
            },
            "transactionLastEvent": {
              "type": "null"
            }
          }
        }
      }
    }
  }
}"""


def FL_CDC_DPL_SHOPPING():
    return """{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "my_topic2",
  "type": "object",
  "properties": {
    "magic": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "headers": {
      "type": "null"
    },
    "messageSchemaId": {
      "type": "null"
    },
    "messageSchema": {
      "type": "null"
    },
    "message": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "ORDER_ID": {
              "type": "integer"
            },
            "PRODUCT_ID": {
              "type": "integer"
            },
            "QUANTITY": {
              "type": "integer"
            },
            "PRICE": {
              "type": "string"
            },
            "CUSTOMER_ID": {
              "type": "integer"
            },
            "ORDER_DATE": {
              "type": "string"
            }
          }
        },
        "beforeData": {
          "type": "null"
        },
        "headers": {
          "type": "object",
          "properties": {
            "operation": {
              "type": "string"
            },
            "changeSequence": {
              "type": "string"
            },
            "timestamp": {
              "type": "string"
            },
            "streamPosition": {
              "type": "string"
            },
            "transactionId": {
              "type": "string"
            },
            "changeMask": {
              "type": "null"
            },
            "columnMask": {
              "type": "null"
            },
            "transactionEventCounter": {
              "type": "null"
            },
            "transactionLastEvent": {
              "type": "null"
            }
          }
        }
      }
    }
  }
}"""
