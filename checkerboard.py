square_nb = 0
rice = 0
rice_sum = 0

for square_nb in range(0,64):

    rice = 2**square_nb
    rice_sum = rice_sum + rice
    print "number of rices on this square :", rice 
    print "square number :", square_nb + 1
    print "total of rices :", rice_sum
    print 
