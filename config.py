# Author: Rafael Bayer (https://github.com/rafibayer)

import json
from types import SimpleNamespace

class Config:
    """
    config.json schema + utility for serialization/deserialization
    """

    def __init__(self, client_id, client_secret, auth_callback_uri, hotkey):
        self.client_id = client_id       
        self.client_secret = client_secret
        self.auth_callback_uri = auth_callback_uri
        self.hotkey = hotkey

    @staticmethod
    def dump(config):
        return json.dumps(config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def load(string):
        return json.loads(string, object_hook=lambda d: SimpleNamespace(**d))