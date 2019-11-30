# Reads the data for sales.txt from the hard drive

def main():
    sales_file = open( "sales.txt", "r" )
    
    for line in sales_file:
        amount = float( line )
        print( format( amount, ".2f" ) )

    sales_file.close()

main()
    
##>>> 
##1000.00
##2000.00
##3000.00
##4000.00
##5000.00
##>>> 
