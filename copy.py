    
def copy():
    print "Which file would you like to copy?"
    file_in = raw_input('> ')
    template = open(file_in, 'r')
    
    print "Where would you like it to go?"
    to_file = raw_input('> ')
    new_file = open(to_file, 'w')
    
    data = template.read()
    new_file.write(data)
    
    new_file.close()
    
