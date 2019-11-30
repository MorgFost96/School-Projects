#This program lists the sales for 5 days

def createList():
    #Teacher put ndays = 5 and sales = [ 0 ] * ndays
    sales = [ 0 ] * 5
    print( "Enter sales for each day" )

    i = 0
    while( i < len( sales ) ):
        print( "Day #", i + 1, ": ", sep = "", end = "" )
        sales[ i ] = float( input( ) )
        i += 1

    return sales

def display( list ):
    print( "Here are the values entered:" )
    for n in list:
        print( n )

def main():
    sales = createList()
    display( sales )

main()

##>>> 
##Enter sales for each day
##Day #1: 1000
##Day #2: 2000
##Day #3: 3000
##Day #4: 4000
##Day #5: 5000
##Here are the values entered:
##1000.0
##2000.0
##3000.0
##4000.0
##5000.0
##>>> 
