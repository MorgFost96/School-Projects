# Writes he data for the sales onto the hard drive

def main():
    num_days = int( input( "For how many days do you have sales? " ) )

    sales_file = open( "sales.txt", "w" )
    
    for count in range( 1, num_days + 1 ):
        sales = float( input( "Enter the sales for day #" + str( count ) + ": " ) )
        sales_file.write( str( sales ) + "\n" )
        
    sales_file.close()
    print( "Data written to sales.txt" )

main()

##>>> 
##For how many days do you have sales? 5
##Enter he sales for day #1: 1000
##Enter he sales for day #2: 2000
##Enter he sales for day #3: 3000
##Enter he sales for day #4: 4000
##Enter he sales for day #5: 5000
##Data written to sales.txt
##>>> 
