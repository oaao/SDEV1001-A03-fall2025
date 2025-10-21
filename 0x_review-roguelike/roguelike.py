"""
OK, so you got horribly pranked by a cruel & mischievous README scroll.

It happens -- it's not like you've never met a troll before; it's just
not how you expected a magic piece of paper to behave. Lesson learned.

But look at the bright side:
Being able to warp the fabric of reality is *pretty* sick. You just need to
figure out a little more about how magic works, and you'll be free in no time. 

Maybe reality might bend to your will more easily if you choose its name?

And while we're at it, let's revoke pranking privileges from that stupid scroll.
*We* get to pick the loading screen for our new reality, thank you very much.
"""


# Variables that are meant to be constants can be written in uppercase,
# to indicate they shouldn't be changed from what is hardcoded in the file.
# This is ONLY a visual convention, and does not affect string behaviour.
#
# Change GAME_NAME to whatever you want.
GAME_NAME = "Dork Souls II: Scholar of the First Git"


# You've heard of f-strings, but what about r-strings?
# Raw strings render text *exactly* as-is, without having to escape characters.
# https://www.w3schools.com/python/gloss_python_escape_characters.asp
#
# Optional: grab some ascii art for your loading screen, and paste it between
# the triple quotes below. (try e.g. https://emojicombos.com/ascii-art)
# 
# Since your ascii art might contain a character that would need to be escaped,
# Using an r-string here prevents the string from breaking.
LOADING_SCREEN = r"""

"""


# '\n' in a string creates a new line. Remember character escaping, just above?
# the '\' escapes whatever character comes after it, so we don't just get 'n'.
#
# Wait... do you even remember who you are?
hero_name = input("\nDo you remember who you are? What is your name, adventurer?\n")



# Now you can run the program. And look! You can *combine* f- and r-strings.
# 'f' for 'format', 'r' for 'raw'. Be fr!
print(fr"""

   Behold, {hero_name}:
   You find yourself in a loveless, timeless void.
      
   By meddling with the mortifying power of the devious README scroll,
   your naïve incantations have broken apart the continuity of time itself!
      
   Is this escape at last?
   Or is it merely the beginning...

         Welcome to...
         =-=-=-=-= {GAME_NAME} =-=-=-=-=

   {LOADING_SCREEN}
                                
""")
