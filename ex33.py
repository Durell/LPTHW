def num_list(x):
    i = 0
    numbers = []
    
    while i < x:
        print "At the top is %d" % i
        numbers.append(i)
    
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "
    
    for num in numbers:
        print num
