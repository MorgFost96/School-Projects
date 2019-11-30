#Allows the user to enter the start and end range then calculates the squares
#of each number in the range

#Input
start = int( input( "Enter a start value: " ) )
end = int( input( "Enter an end value: " ) )

#Output
print( "Number\tSquare" )

for num in range( start, end + 1 ):
    square = num ** 2
    print( num, '\t', square, sep = '' )

##>>> 
##Enter a start value: 5
##Enter an end value: 10
##Number	Square
##5	25
##6	36
##7	49
##8	64
##9	81
##10	100
##>>> 
