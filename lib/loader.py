from dotenv import *

class theLoader:
    def __init__(self, file_location):
        config = dotenv_values(file_location)
        self.sanitizedConfig = self.sanitize(config)

    def getConfig(self):
        return self.sanitizedConfig

    ## Fixes dotenv load everything as a string
    @staticmethod
    def sanitize(config):
        for key in config:
            if config[key] == 'None':
                config[key] = None
            elif config[key] == 'True':
                config[key] = True
            elif config[key] == 'False':
                config[key] = False
            elif config[key].replace('.','',1).isnumeric() == True:
                if '.' in config[key]:
                    config[key] = float(config[key])
                else:
                    config[key] = int(config[key])

        return config
