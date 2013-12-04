people = 30
cars = 40
buses = 15


# us an if statement to determine if value of cars is greater than people
if cars > people:
    # if above is true, statement below will print out
    print "We should take the cars."
# if above is false check if cars are greater than people
elif cars < people:
    # print below statement if cars < people
    print "We should not take the cars."
# this will run when both 'if' and 'elif' statements return false
else:
    print "We can't decide."

# check to see if value of buses is greater than cars. If true will run print
if buses > cars:
    print "That's too many buses."
# when above statement returns false, check if buses are greater than cars
# and print string if true
elif buses < cars:
    print "Maybe we should take the buses."
# print string if both value checks above return false.
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
