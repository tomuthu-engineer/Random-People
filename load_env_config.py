from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
DB_NAME = os.getenv('DB_NAME')