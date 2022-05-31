import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bearer_token = os.environ.get("BEARER_TOKEN")
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")