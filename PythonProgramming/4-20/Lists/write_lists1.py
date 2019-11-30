# Saving Lists to File

def main():
    cities = [ "New York", "Boston", "Atlanta" ]
    outfile= open( "cities.txt", "w" )
    outfile.writelines( cities )
    outfile.close()

main()
