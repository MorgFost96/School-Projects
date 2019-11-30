# Save List of Numbers

def main():
    num = [ 1, 2, 3, 4, 5, 6, 7 ]
    outfile = open( "numlist.txt", "w" )

    for item in num:
        outfile.write( str( item ) + "\n" )

    outfile.close()

main()
