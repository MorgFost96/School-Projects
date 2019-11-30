#Morgan Foster
#1021803
# Exam 3 Program 2

def load():
    sh = int( input( "Stock Shares: " ) )
    bp = float( input( "Purchase Price: " ) )
    sp = float( input( "Selling Price: " ) )
    rate = float( input( "Broker Percentage Commision: " ) )
    return sh, bp, sp, rate

def calc( sh, bp, sp, rate ):
    num_paid = sh * bp
    com_paid = num_paid * ( rate / 100 )
    num_sold = sh * sp
    com_sold = num_sold * ( rate / 100 )
    pr = ( num_sold - com_sold ) - ( num_paid + com_paid )
    return num_paid, com_paid, num_sold, com_sold, pr

def output( name, num_paid, com_paid, num_sold, com_sold, pr ):
    print( "" )
    print( "Stock Name:", name )
    print( "Amount Paid for Stock: $", format( num_paid, ",.2f" ), sep = "" )
    print( "Commission for Buying: $", format( com_paid, ",.2f" ), sep = "" )
    print( "Amount Stock Sold for: $", format( num_sold, ",.2f" ), sep = "" )
    print( "Commission for Selling: $", format( com_sold, ",.2f" ), sep = "" )
    print( "Money Remaining: $", format( pr, ",.2f" ), sep = "" )
    print( "" )
    print( "" )

def main():
    
    tp = 0.0
    name = input( "Stock Name (Type 'Quit' to Stop): " )
    while( name != "Quit" ):
        sh, bp, sp, rate = load()
        num_paid, com_paid, num_sold, com_sold, pr = calc( sh, bp, sp, rate )
        output( name, num_paid, com_paid, num_sold, com_sold, pr )
        tp = tp + pr
        name = input( "Stock Name (Type 'Quit' to Stop): " )

    print( "\nTotal Profit:", tp )

main()

##>>> 
##==== RESTART: D:\School\2016 - 17\Python\Homework\Exam 3\exam3program1.py ====
##Stock Name (Type 'Quit' to Stop): Test1
##Stock Shares: 10
##Purchase Price: 100
##Selling Price: 200
##Broker Percentage Commision: 10
##
##Stock Name: Test1
##Amount Paid for Stock: $1,000.00
##Commission for Buying: $100.00
##Amount Stock Sold for: $2,000.00
##Commission for Selling: $200.00
##Money Remaining: $700.00
##
##
##Stock Name (Type 'Quit' to Stop): Test2
##Stock Shares: 20
##Purchase Price: 50
##Selling Price: 75
##Broker Percentage Commision: 5
##
##Stock Name: Test2
##Amount Paid for Stock: $1,000.00
##Commission for Buying: $50.00
##Amount Stock Sold for: $1,500.00
##Commission for Selling: $75.00
##Money Remaining: $375.00
##
##
##Stock Name (Type 'Quit' to Stop): Quit
##
##Total Profit: 1075.0
##>>> 
