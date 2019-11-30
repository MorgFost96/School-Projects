#This program finds the max number that a user inputs

#Input
num = int( input( "Enter a number (-999 to stop): " ) )
max = num

#Calc/Processing
while ( num != -999 ):
    if ( num > max ):
        max = num
    num = int( input( "Enter a number (-999 to stop): " ) )

#Output
print( "The maximum number is", max )

##>>> 
##Enter a number (-999 to stop): 10
##Enter a number (-999 to stop): 20
##Enter a number (-999 to stop): 30
##Enter a number (-999 to stop): 20
##Enter a number (-999 to stop): -999
##The maximum number is 30
##>>> 
