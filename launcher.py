from __future__ import unicode_literals

from configurations.seleniumconfigs import *
from services.facebook.AccountInfo import *
import getopt

def initialize(args):
    try:
        args.remove(args[0])
        optlist, args = getopt.getopt(args, 'fc', ['loggermode=', 'configs='])
        for opt, val in optlist:
            if opt == "-c" or opt == "-f":
                Logger().setLoggeroutput(opt)
            elif opt == "--loggermode":
                Logger().setLoggermode(val)
            elif opt == "--configs":
                Configuration().__init__(val)
    except getopt.GetoptError as err:
        print(str(err))

    log.INFO("Initializing application...")

    SeleniumConfigs().initializeconfigs()

    log.INFO("Initializing completed.")


def execute():
    displayer = AccountInfo(SeleniumConfigs().driver_location, SeleniumConfigs().action_delay)
    displayer.signin(SeleniumConfigs().login, SeleniumConfigs().password)
    displayer.get_friends_dict()
    displayer.finalize()


if __name__ == "__main__":
    initialize(sys.argv)
    execute()
