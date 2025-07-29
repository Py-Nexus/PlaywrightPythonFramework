import os
from configparser import ConfigParser
from functools import lru_cache

@lru_cache()
def load_config():
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "..", "configdata", "conf.ini")
    config.read(config_path)
    return config

def read_config(section, key):
    config = load_config()
    return config.get(section, key)