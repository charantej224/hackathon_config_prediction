import json


class Collective(object):
    def __init__(self, deployment, expansion, update):
        self.deployment = deployment
        self.expansion = expansion
        self.update = update

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
