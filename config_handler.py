import configparser
from collections.abc import Collection
import warnings

class ConfigHandler:

    def __init__(self, config_names: Collection[str], configfile_addresses: Collection[str]):
        self.configs = {}
        self.config_names = config_names
        self.config_addresses = {}

        for name, address in zip(config_names, configfile_addresses):
            self.config_addresses[name] = address
            new_config = configparser.ConfigParser(address)
            new_config.read(address)
            self.configs[name] = new_config
    
    def add_config(self, config_dictionary):
        # Create a config based on the given dictionary
        pass

    def set_config(self):
        # will not right the changes on the file
        pass

    def get_config(self):
        pass

    def save_config(self, name):
        with open(self.config_addresses[name]) as config_file:
            self.configs[name].write(config_file)

    def save_configs(self):
        for config_name in self.config_names:
            self.save_config(config_name)
                
    def __getitem__(self, key):
        return self.configs[key]
    
    def __hash__(self, key):
        # This is incorrect
        # Not hashable because of having dictionaries
        return hash(id(self))