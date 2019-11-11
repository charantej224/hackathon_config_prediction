import json


class Reliability(object):
    def __init__(self, product_name, result, difference):
        self.product_name = product_name
        self.result = result
        self.difference = difference

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
