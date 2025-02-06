import configparser
import os

path = os.path.join(os.path.dirname(__file__), '../config/config.conf')

config = configparser.ConfigParser()
config.read(path)

## Reddit Api Config
SECRET_KEY = config.get('reddit','REDDIT_SECRET_KEY')
CLIENT_KEY = config.get('reddit','REDDIT_CLIENT_ID')
REDDIT_AGENT = config.get('reddit','REDDIT_AGENT')

## Database config
POSTGRESQL_USERNAME = config.get('database', 'POSTGRESQL_USERNAME')
POSTGRESQL_PASSWORD = config.get('database', 'POSTGRESQL_PASSWORD')
POSTGRESQL_DATABASE = config.get('database', 'POSTGRESQL_DATABASE')
POSTGRESQL_HOST = config.get('database', 'POSTGRESQL_HOST')
POSTGRESQL_PORT = config.get('database', 'POSTGRESQL_PORT')