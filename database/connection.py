from sqlalchemy import URL
from dotenv import load_dotenv
import os

load_dotenv()

db_url = URL.create(
    'mysql',
    database=os.getenv('DB_NAME'),
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST')
)