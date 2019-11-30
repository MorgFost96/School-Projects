# Write data to friends.txt

def main():
    print( "Enter the names of 3 friends")
    name1 = input( "Friend 1: " )
    name2 = input( "Friend 2: " )
    name3 = input( "Friend 3: " )
    
    myfile = open( "friends.txt", "w" )   # Open
    
    myfile.write( name1 + "\n" )     # Write
    myfile.write( name2 + "\n" )
    myfile.write( name3 + "\n" )

    myfile.close                       # Close File

    print( "\nData written to file" )

main()
