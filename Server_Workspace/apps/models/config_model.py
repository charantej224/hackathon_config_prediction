import json


class ConfigData(object):
    def __init__(self, product_name, month, day, count, cores, storage):
        self.product_name = product_name
        self.month = month
        self.day = day
        self.count = count
        self.cores = cores
        self.storage = storage

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
