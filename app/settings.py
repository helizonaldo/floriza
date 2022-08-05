import os 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

config_object  = os.getenv('APP_SETTINGS')


from abc import ABC
class BaseConfig(ABC):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = os.getenv('SECRET_KEY')
	

class DevelopmentConfig(BaseConfig):

	DEBUG = True
	DEVELOPMENT = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///banco.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
	DEBUG = False
	DEVELOPMENT = False
	SECRET_KEY = os.getenv('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///memory'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_ECHO = True
