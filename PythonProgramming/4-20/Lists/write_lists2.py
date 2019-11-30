# Saving Lists to File

def main():
    cities = [ "New York", "Boston", "Atlanta" ]
    outfile= open( "cities.txt", "w" )

    for item in cities:
        outfile.write( item + "\n" )

    outfile.close()

main()
