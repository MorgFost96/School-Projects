#Star Pyramid

#Imports
import random

#Input
base = int( input( "What is the base? " ) )

#Output
##for row in range( 0, base ):
##    print( "*" * (row + 1)  )

print()
for row in range( 0, base ):
    for col in range( 0, row + 1 ):
        print( "*", end = '' )
    print()

print()
for row in range( 0, base ):
    for col in range( 0, base - row ):
        print( "*",  end = '' )
    print()

print()
for row in range( 0, base ):
    for col in range( 0, row ):
        print( " ", end = '' )
    for col in range( 0, base - row ):
        print( "*", end = '' )
    print()

print()
for row in range( 0, base ):
    for col in range( 0, base - (row + 1) ):
        print( " ", end = '' )
    for col in range( 0, row + 1 ):
        print( "*", end = '' )
    print()
