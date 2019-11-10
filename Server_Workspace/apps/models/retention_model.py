import json


class Retention(object):
    def __init__(self, customer_id, result, count):
        self.customer_id = customer_id
        self.result = result
        self.count = count

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
