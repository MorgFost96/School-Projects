#This program calculates the area of a triangle

def triangleArea( base, height ):
    return 0.5 * base * height

def main():
    b = float( input( "Base: " ) )
    h = float( input( "Height: " ) )
    print( "Area: ", triangleArea( b, h ) )

main()

##>>> 
##Base: 10
##Height: 5
##Area:  25.0
##>>> 
