from __future__ import unicode_literals
from configurations.configuration import *
from utils.singleton import singleton


@singleton
class SeleniumConfigs:
    def __init__(self):
        pass

    def initializeconfigs(self):
        try:
            configs = Configuration().configs
            self.driver_location = configs["driver_location"]
            self.action_delay = configs["action_delay"]
            self.login = configs["login"]
            self.password = configs["password"]
            log.INFO("Configurations for selenium loaded.")
        except KeyError as err:
            log.ERROR("Configuration does not fits arguments. {}".format(str(err)))
            sys.exit(1)
