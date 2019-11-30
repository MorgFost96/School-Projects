#Function Examples

#Example 1
def message():
    print( "I am great!" )
    print( "King of the Nords!" )

message()

##>>> 
##I am great!
##King of the Nords!
##>>> 

#Example 2
##def main():
##    print( "I have a message for you" )
##    message()
##    print( "Goodbye" )
##
##main()

##>>> 
##I have a message for you
##I am great!
##King of the Nords!
##Goodbye
##>>> 

#Example 3
def sum( i1, i2 ):
    result = 0
    for i in range( i1, i2 + 1 ):
        result += i
    return result

def main():
    print( "Sum from 1 to 10", sum( 1, 10 ) )

