# 2D Arrays

import random

rows = 3
cols = 4

def main():
    values = [ [ 0 for c in range( cols ) ] for r in range( rows ) ]
    
    for r in range( rows ):
        for c in range( cols ):
            values[ r ][ c ] = random.randint( 1, 100 )

    print( values )

def automatic_list():
    values = []
    for r in range( rows ):
        values.append([])
        for c in range( cols ):
            values[ r ].append( 0 )

main()
