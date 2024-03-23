import os
from dotenv import load_dotenv


load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
fortochki_login = os.getenv('FORTOCKI_LOGIN')
fortochki_password = os.getenv('FORTOCKI_PASSWORD')