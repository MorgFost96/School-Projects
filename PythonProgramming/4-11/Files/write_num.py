# Writes to num.txt

def main():
    outfile = open( "num.txt", "w" )
    num1 = int( input( "Enter a number: " ) )
    num2 = int( input( "Enter a number: " ) )
    num3 = int( input( "Enter a number: " ) )

    outfile.write( str( num1 ) + "\n" )
    outfile.write( str( num2 ) + "\n" )
    outfile.write( str( num3 ) + "\n" )

    outfile.close()
    print( "\nData written to file" )

main()
