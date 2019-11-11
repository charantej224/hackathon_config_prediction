import json


class Data(object):
    def __init__(self, product_name, count):
        self.product_name = product_name
        #self.month = month
        #self.day = day
        self.count = count

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
