import os
from dotenv import load_dotenv
load_dotenv()

class BaseConfig:
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv("DEV_MONGO_URI")