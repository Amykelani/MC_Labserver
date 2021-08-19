from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')
MAX_CONTENT_LENGTH = 10 * 1000 * 1000
ALLOWED_EXTENSIONS = {'json', 'xdl', 'png'}
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
JSON_AS_ASCII = False

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
