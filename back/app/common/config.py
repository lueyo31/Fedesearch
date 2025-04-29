import os
from dotenv import load_dotenv
load_dotenv()
VERSION = os.getenv('VERSION')
API_VERSION = os.getenv('API_VERSION')
SEARCH_API_URL = os.getenv('SEARCH_API_URL')
SELF_HOST = f"{os.getenv('SELF_URL')}:{os.getenv('SELF_PORT')}"
FRONTEND_URL = os.getenv('FRONTEND_URL')