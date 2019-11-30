#Morgan Foster
#1021803
#
# Exam 3 Program 1

def isPalindrome( s ):
    low = 0
    high = len( s ) - 1

    while( low < high ):
        if( s[ low ].upper() != s[ high ].upper() ):
            return False
        low += 1
        high -= 1
    
    return True

def main():
    s = input( "String: " )
    if( isPalindrome( s ) ):
        print( s, "is a Palindrome" )
    else:
        print( s, "is not a Palindrome" )

main()

##>>> 
##String: Rats live on no evil star
##Rats live on no evil star is a Palindrome
##>>> 
##String: Test
##Test is not a Palindrome
##>>> 
