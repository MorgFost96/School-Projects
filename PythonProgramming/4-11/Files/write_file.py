# Writes data to file.txt

def main():
    outfile = open( "file.txt", "w" )   # Open
    
    outfile.write( "John Locke\n" )     # Write
    outfile.write( "David Hume\n" )
    outfile.write( "Edmund Burke\n" )

    outfile.close                       # Close File

main()
