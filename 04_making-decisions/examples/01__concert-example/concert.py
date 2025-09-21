# remember to look at the commit history for this file
# to see how the example was developed step-by-step.

concert_name = input("What is the name of the concert? ")
has_ticket = input("Do you have a ticket? (y/n) ")

if concert_name == "taylor swift" and has_ticket == "y":
    print("you're in the right place")
    print("have fun!")
if concert_name == "taylor swift" and has_ticket == "n":
    print("you need a ticket, bestie")
elif concert_name == "billie eilish":
    print("that concert is next door")
elif concert_name == "ozzy reanimation tour":
    print("R.I.P. dark prince")
else:
    print("this is not the concert you're looking for")
