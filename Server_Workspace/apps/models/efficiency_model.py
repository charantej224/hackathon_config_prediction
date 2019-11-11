import json


class Efficiency(object):
    def __init__(self, product_name, result, count):
        self.product_name = product_name
        self.result = result
        self.count = count

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
