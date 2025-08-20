# src/config.py

import os
from dotenv import load_dotenv

def load_env():
    """
    Load environment variables from the .env file.
    Call this once at the start of your program or notebook.
    """
    load_dotenv()

def get_key(key_name: str, default=None):
    """
    Retrieve a variable from the environment.
    Example: get_key("API_KEY")
    """
    return os.getenv(key_name, default)