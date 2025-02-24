'''Configuration module.
'''
from typing import Any

import dotenv


def load_config() -> dict[str, Any]:
    '''Load the configuration from the .env file
    '''
    env = dotenv.dotenv_values()
    return env
