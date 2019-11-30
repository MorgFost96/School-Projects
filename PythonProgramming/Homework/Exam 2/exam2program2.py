#Morgan Foster
#1021803
#This program allows the user to input stock information until the user is
#chooses to stop, then outputs calculations for the stocks that the user input.

#Input
name = "default"

while( name != "Quit" ):
    name = input( "Stock Name (Type 'Quit' to Stop): " )
    if( name != "Quit" ):
        shares = int( input( "Stock Shares: " ) )
        buyPrice = float( input( "Purchase Price: " ) )
        sellPrice = float( input( "Selling Price: " ) )
        commission = float( input( "Broker Percentage Commision: " ) )

        #Calc/Processing
        amtPaid = shares * buyPrice
        paidCommission = amtPaid * ( commission / 100 )
        amtSold = shares * sellPrice
        soldCommission = amtSold * ( commission / 100 )
        profit = ( amtSold - soldCommission ) - ( amtPaid + paidCommission )

        #Output
        print( "" )
        print( "Stock Name:", name )
        print( "Amount Paid for Stock: $", format( amtPaid, ",.2f" ), sep = "" )
        print( "Commission for Buying: $", format( paidCommission, ",.2f" ), sep = "" )
        print( "Amount Stock Sold for: $", format( amtSold, ",.2f" ), sep = "" )
        print( "Commission for Selling: $", format( soldCommission, ",.2f" ), sep = "" )
        print( "Money Remaining: $", format( profit, ",.2f" ), sep = "" )
        print( "" )
        print( "" )

##>>> 
##==== RESTART: D:\School\2016 - 17\Python\Homework\Exam 2\exam2program2.py ====
##Stock Name (Type 'Quit' to Stop): Test
##Stock Shares: 10
##Purchase Price: 100
##Selling Price: 200
##Broker Percentage Commision: 10
##
##Stock Name: Test
##Amount Paid for Stock: $1,000.00
##Commission for Buying: $100.00
##Amount Stock Sold for: $2,000.00
##Commission for Selling: $200.00
##Money Remaining: $700.00
##
##
##Stock Name (Type 'Quit' to Stop): Quit
##>>> 
