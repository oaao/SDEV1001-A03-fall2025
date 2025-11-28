import os

# I've installed dotenv into my virtualenv via pip,
# and if I run programs from my virtualenv, I can just import
# the dotenv package and use stuff from it!
from dotenv import load_dotenv



# a function to read environment variables using python's built-in module 'os'
# (os -> for Operating System stuff)
def get_config():
    load_dotenv()  
    return {
        "title": os.getenv("APP_TITLE", "missing APP_TITLE"),
        "author": os.getenv("AUTHOR", "missing_author")
    }
