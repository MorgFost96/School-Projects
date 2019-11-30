#This program calculates the sum and average with a flag

#Input
count = 0
sum = 0
num = int( input( "Enter a number (-999 to exit): " ) )

#Calc/Processing
while( num != -999 ):
    sum += num
    num = int( input( "Enter a number (-999 to exit): " ) )
    count += 1

if count != 0:
    avg = float( sum / count )
else:
    avg = 0

#Output
print( "You input:", count, "numbers" )
print( "The total is:", sum )
print( "The average is:", avg )

##>>> 
##Enter a number (-999 to exit): -999
##You input: 0 numbers
##The total is: 0
##The average is: 0
##>>> 
##Enter a number (-999 to exit): 10
##Enter a number (-999 to exit): 20
##Enter a number (-999 to exit): 30
##Enter a number (-999 to exit): -999
##You input: 3 numbers
##The total is: 60
##The average is: 20.0
##>>> 
