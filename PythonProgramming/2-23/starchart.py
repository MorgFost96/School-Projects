#Star Pyramid

import random

#Input
base = int( input( "What is the base? " ) )

#Normal Pyramid
print()
for i in range( 0, base ):
    print( "   |", end = '' )
    print( " ", i, " ", sep = '', end = '')
    
print( "\n----", "-" * (base * 2), sep = '' )
for row in range( 0, base ):
    for col in range( 0, row + 1 ):
        if( col == 0 ):
            print( r, " ", end = '' )
        print( "*", end = '' )
    print()

#Chart
print( "Chart for the first Pyramid\n" )
print( "r\t\tc\t\tout" )
print( "-\t\t-\t\t---" )
for row in range( 0, base ):
    for col in range( 0, row + 1 ):
        print( row, "\t\t", sep = '', end = '' )
        print( col, "\t\t", sep = '', end = '' )
        print( "*")
    print( row, "\t\t", sep = '', end = '' )
    print( col + 1, "\t\t", sep = '', end = '' )
    print( "\\n\n" )
