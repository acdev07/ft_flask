from config.base_config import BaseConfig
import os

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGO_URI = os.getenv("DEV_MONGO_URI")