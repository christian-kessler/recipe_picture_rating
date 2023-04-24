'''
  Copyright ©2019, Überfein UG (haftungsbeschränkt) - All rights reserved.
'''

import os

from configparser import ConfigParser

script_dir = os.path.dirname(__file__)
rel_path = './config.ini'
abs_file_path = os.path.join(script_dir, rel_path)

# Environments
section_prod = 'production'
section_dev = 'development'

# Env Vars
MY_NAME = 'my_name'
MY_PORT = 'my_port'
GATEWAY_HOST = 'gateway_host'
GATEWAY_URL = 'gateway_url'
REGISTRY_URL = 'registry_url'
DO_REGISTRATION = 'do_registration'


# Env to set on the pro machine
DEKU_ENV = 'DEKU_ENV'


def create_config(file_path=abs_file_path):
    parser = ConfigParser()
    parser.read(file_path)

    config = {}

    section = section_dev
    try:
        section = os.environ[DEKU_ENV]
    except:
        pass

    print('Running on {0} mode'.format(section))

    if not section:
        section = "development"

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(
            section, 'config.ini'))

    return config


config = create_config()
