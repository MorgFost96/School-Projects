# Reads List of Numbers

def main():
    infile = open( "numlist.txt", "r" )

    num = infile.readlines()
    infile.close()
    index = 0
    while index < len( num ):
        num[ index ] = int( num[ index ] )
        index += 1

    print( num )

main()

##>>> 
##[1, 2, 3, 4, 5, 6, 7]
##>>> 
