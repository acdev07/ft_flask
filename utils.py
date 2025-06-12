import os
from typing import Dict

from dotenv import load_dotenv

load_dotenv()

def loadConfig() -> Dict[str, str]:
    """
    Load configuration from the .env file

    :return: A dictionary of configuration settings
    """
    return {
        "SECRET_API_KEY": os.getenv("SECRET_API_KEY")
    }
