import os
from instabot import InstaBot
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the login and password from the environment variables
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

bot = InstaBot(login=login, password=password,
               like_per_day=1000,
               max_like_for_one_tag=5,
               follow_per_day=150,
               follow_time=5*60*60,
               unfollow_per_day=150,
               comments_per_day=50,
               tag_list=['girl', 'car', 'cat'],
               log_mod=0)

bot.new_auto_mod()
