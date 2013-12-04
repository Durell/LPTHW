# import argv from sys module
from sys import argv

# set variables for argv
script, input_file = argv

# create a function named print-all that takes paramater f
def print_all(f):
    # print the output of the .read() on paramater f
    print f.read()

# create a function named rewind that takes paramater f
def rewind(f):
    # use seek to get to the first position of paramater f
    f.seek(0)

# create function print_a_line that takes parameters line_count and f
def print_a_line(line_count, f):
    # print the output of line_count and readline() of f on the same line
    print line_count, f.readline()

# create variable current_file and set it to open input_file from argv
current_file = open(input_file)

# print message letting us know that we're going to print the whole file
print "First let's pring the whole file:\n"

# use the print_all function with the current_file variable passed as a parameter
print_all(current_file)

# print message letting us know that we're going to 'rewind' to the beginning
# of the file
print "Now let's rewind, kind of like a tape."

# use rewind function to seek to the first position in the current_file variable
rewind(current_file)

# print message letting us know that we're going to print out lines individually
print "Let's print three lines:"

# create current_line variable and set it to value of 1
current_line = 1
# use the print_a_line function with current_line and current_file variables 
# passed as parameters. The function is set to print both out on the same line
print_a_line(current_line, current_file)

# set current line variable to itself + 1 allowing us to count up creating a list
current_line = current_line + 1
# once again pass variables as parameters to print_a_line function to print
print_a_line(current_line, current_file)

# repeat of above two steps
current_line = current_line + 1
print_a_line(current_line, current_file)
