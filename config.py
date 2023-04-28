import os

from dotenv import load_dotenv

load_dotenv()
PATH_FILE = os.getenv('PATH_FILE')


class DefaultConfig(object):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    DEBUG = False
