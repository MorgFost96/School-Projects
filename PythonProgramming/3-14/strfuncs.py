#String Funcion Example

import random

s = "Welcome"
print( len( s ) )
print( max( s ) )
print( min( s ) )

for i in range( 0, len( s ), 2 ):
    print( s[i], end = "" )

print()
print( s[-1] )
print()

word = "index"
print( "The word is", word, "\n" )
high = len( word )
low = -len( word )

for i in range( 10 ):
    pos = random.randrange( low, high )
    print( "word[", pos, "]\t", word[pos] )

print( s[ 1 : 4 ] )
print( s[ : 6 ] )
print( s[ 4 : ] )
print( s[ 1 : -1 ] )    #Better to write print( s[ 1 : len( s ) - 1 ] )

s2 = "Python"
s3 = s + "to" + s2      #No Spaces
s4 = s * 3              #WelcomeWelcomeWelcome
s5 = 3 * s              #s4

s = input( "Enter a String" )
if( "Python" in s ):
    print( "Pyhon is in", s )
else:
    print( "Python not in", s )

##>>> 
##7
##o
##W
##Wloe
##e
##
##The word is index 
##
##word[ -2 ]	 e
##word[ -2 ]	 e
##word[ 1 ]	 n
##word[ -2 ]	 e
##word[ 4 ]	 x
##word[ -3 ]	 d
##word[ -3 ]	 d
##word[ -5 ]	 i
##word[ 3 ]	 e
##word[ 4 ]	 x
##elc
##Welcom
##ome
##elcom
##>>> 
