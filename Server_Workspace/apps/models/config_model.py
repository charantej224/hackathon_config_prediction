import json


class ConfigData(object):
    def __init__(self, product_name, count, configuration):
        self.product_name = product_name
        self.configuration = configuration
        self.count = count

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
