import os
import configparser
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--cookies_name', type=str, default='')
parser.add_argument('--config_name', type=str, default='config.ini')
args = parser.parse_args()
cookies_name = args.cookies_name
config_name = args.config_name

print(cookies_name)
print(config_name)

class Config(object):
    def __init__(self, config_file=config_name):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: {}", config_name)
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)


global_config = Config()
