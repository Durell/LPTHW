# print message asking to choose between doors 1 or 2
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

# set variable door to output of raw input
door = raw_input("> ")

# set up script to execute if the door variable was set to "1"
if door == "1":
    # Set up setting inside room
    print "There's a giant bear here eating a cheese cake. What do you do?"
    # give options for how to deal with the bear.
    print "1. Take the cake."
    print "2. Scream at the bear."

    # set output of raw_input to the variable bear
    bear = raw_input("> ")

    # Set up what to do depending on how user responds to raw_input
    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

# set up what should happen if door 2 was chosen at beginning of script
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    # extra credit - added two options to work with to create elif below
    print "4. kill kill kill"
    print "5. cool cool cool"

    insanity = raw_input("> ")

    if insanity == "1": 
        print "Your body survives powered by a mind of jello. Good job!"
    # extra credit - created elif to check if the integer of the string in the
    # insanity variable is in between 2 and 4. 
    elif int(insanity) in range(2, 5):
        print "It worked!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
