# Read data from file.txt

def main():
    infile = open( "file.txt", "r" )
    file_contents = infile.read()
    infile.close()

    print( file_contents )

main()
