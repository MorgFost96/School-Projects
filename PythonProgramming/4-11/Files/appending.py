# Appends data to friends.txt

def main():
    myfile = open( "friends.txt", "a" )
    myfile.write( "Then\n" )
    myfile.write( "Appending\n" )
    myfile.close()

main()
