from configparser import ConfigParser

global_config: ConfigParser = ConfigParser()
global_config.read("config/dev.ini")
