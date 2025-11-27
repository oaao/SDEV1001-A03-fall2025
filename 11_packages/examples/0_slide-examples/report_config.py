import os

# I've installed dotenv into my virtualenv via pip,
# and if I run programs from my virtualenv, I can just import
# the dotenv package and use stuff from it!
from dotenv import load_dotenv



# a function to read environment variables using python's built-in module 'os'
# (os -> for Operating System stuff)
def get_config():
    return {
        "title": os.getenv("APP_TITLE", "missing APP_TITLE"),
        "author": os.getenv("AUTHOR", "missing_author")
    }



# 1. I'm going to run get_config() before loading them in
print(get_config())


# 2. I'm going to load those environment variables using
# dotenv.load_dotenv(), part of the dotenv package
load_dotenv()  
print("dotenv.load_dotenv() called...")
# it looks for an .env file in the same directory, and loads all environment variables
# into the runtime of this program!


# 3. Call our get_config() function again to check
print(get_config())
