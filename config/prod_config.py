from config.base_config import BaseConfig
import os

class ProductionConfig(BaseConfig):
    DEBUG = False
    MONGO_URI = os.getenv("PROD_MONGO_URI")