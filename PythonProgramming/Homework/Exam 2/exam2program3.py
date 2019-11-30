#Morgan Foster
#1021803
#This program allows the user to choose how many stocks they would like to
#input then outputs calculations for the stocks that the user inputs.

stocks = int( input( "How many stocks do you want to enter now? " ) )
print( "" )

for n in range( 0, stocks ):
    #Input
    name = input( "Stock Name: " )
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
##How many stocks do you want to enter now? 3
##
##Stock Name: One
##Stock Shares: 10
##Purchase Price: 100
##Selling Price: 200
##Broker Percentage Commision: 10
##
##Stock Name: One
##Amount Paid for Stock: $1,000.00
##Commission for Buying: $100.00
##Amount Stock Sold for: $2,000.00
##Commission for Selling: $200.00
##Money Remaining: $700.00
##
##
##Stock Name: Two
##Stock Shares: 100
##Purchase Price: 10
##Selling Price: 20
##Broker Percentage Commision: 10
##
##Stock Name: Two
##Amount Paid for Stock: $1,000.00
##Commission for Buying: $100.00
##Amount Stock Sold for: $2,000.00
##Commission for Selling: $200.00
##Money Remaining: $700.00
##
##
##Stock Name: Three
##Stock Shares: 50
##Purchase Price: 10
##Selling Price: 50
##Broker Percentage Commision: 50
##
##Stock Name: Three
##Amount Paid for Stock: $500.00
##Commission for Buying: $250.00
##Amount Stock Sold for: $2,500.00
##Commission for Selling: $1,250.00
##Money Remaining: $500.00
##
##
##>>> 
