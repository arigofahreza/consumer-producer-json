class DictToObj:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)


def to_dict(object, ctx) -> dict:
    return vars(object)
