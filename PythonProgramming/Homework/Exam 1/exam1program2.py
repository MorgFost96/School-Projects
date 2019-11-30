#Morgan Foster
#1021803
#This program calculates the total amount of a meal purchased at a restaurant

#Input
cost = float( input( "Enter the chage for food: $" ) )
TIP = 15.00
TAX = 7.25

#Calc/Processing
tiptotal = TIP / 100 * cost
taxtotal = TAX / 100 * cost
total = cost + tiptotal + taxtotal

#Output
print( "Tip:", format( TIP, '.2f' ), "percent" )
print( "Tax:", format( TAX, '.2f' ), "percent" )
print( "Total Bill : $", format( total, '.2f'), sep = '' )

##>>> 
##Enter the chage for food: $100
##Tip: 15.00 percent
##Tax: 7.25 percent
##Total Bill : $122.25
##>>> 
