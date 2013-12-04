# set variable x to a string with an integer variable insterted
x = "There are %d types of people." % 10
# set binary and do_not variables to strings of same name
binary = "binary"
do_not = "don't"
# set variable y to string using with string variables inserted into it.
y = "Thos who know %s and those who %s." % (binary, do_not)

# print strings from variables x and y
print x
print y

# print string from variable x into another string as raw data 
print "I said: %r." % x
# print string from variable y into another string as a string
print "I also said: '%s'." % y

# set variable hilarious to false
hilarious = False
# set variable joke_evaluation to a string that takes in raw data as an argument
joke_evaluation = "Isn't that joke so funny?! %r"

# print variable joke_evaluation string and insert variable hilarious in the
# raw data for joke_evaluation 
print joke_evaluation % hilarious

# create variables 'w' and 'e' for demonstrating strings below
w = "This is the left side of..."
e = "a string with a right side."

# use the '+' operand can combine variables and strings
print w + e
