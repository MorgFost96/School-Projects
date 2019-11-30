#Morgan Foster
#1021803
#This program calculates the costs of puchasing a user-inputed stock

#Input
name = input( "Enter Stock name : " )
shares = int( input( "Enter Number of shares : " ) )
purchaseprice = float( input( "Enter Purchase price : " ) )
sellingprice = float( input( "Enter selling price : " ) )
commission = float( input( "Enter Commission : " ) )

#Calc/Processing
amtpaid = shares * purchaseprice
commissionpaid = amtpaid * commission
amtsold = shares * sellingprice
commissionsold = amtsold * commission
profit = amtsold - amtpaid - ( commissionpaid + commissionsold )

#Output
print( "\n\nStock Name:", name )
print( "\nAmount paid for the stock:     $", format( amtpaid, '10,.2f' ) )
print( "Commission paid on he puchase: $", format( commissionpaid, '10,.2f' ) )
print( "Amount the stock sold for:     $", format( amtsold, '10,.2f' ) )
print( "Commission paid on the sale:   $", format( commissionsold, '10,.2f' ) )
print( "Profit (or loss if negative):  $", format( profit, '10,.2f' ) )

##>>> 
##Enter Stock name : Kaplack, Inc.
##Enter Number of shares : 10000
##Enter Purchase price : 33.92
##Enter selling price : 35.92
##Enter Commission : 0.04
##
##
##Stock Name: Kaplack, Inc.
##
##Amount paid for the stock:     $ 339,200.00
##Commission paid on he puchase: $  13,568.00
##Amount the stock sold for:     $ 359,200.00
##Commission paid on the sale:   $  14,368.00
##Profit (or loss if negative):  $  -7,936.00
##>>> 
