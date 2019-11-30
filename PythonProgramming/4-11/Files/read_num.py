# Uses num.txt for calculations

def main():
    infile = open( "num.txt", "r" )

    num1 = int( infile.readline() )
    num2 = int( infile.readline() )
    num3 = int( infile.readline() )

    infile.close()

    total = num1 + num2 + num3
    
    print( "Num1:", num1 )
    print( "Num2:", num2 )
    print( "Num3:", num3 )
    print( "Sum:", total )

main()
