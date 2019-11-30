#This program calculates the gross pay
#for each of Megan's Baristas

NUM_EMPLOYEES = 6

def main():
    hours = [ 0 ] * NUM_EMPLOYEES

    for index in range( NUM_EMPLOYEES ):
        print( "Enter the hours woked by employee ",\
               index + 1, ": ", sep = "", end = "" )
        hours[ index ] = float( input() )

    pay_rate = float( input( "Enter the hourly pay rate: " ) )

    for index in range( NUM_EMPLOYEES ):
        gross_pay = hours[ index ] * pay_rate
        print( "Gross pay for employee", index + 1, ": $",\
               format( gross_pay, ",.2f" ), sep = "" )

main()

##>>> 
##Enter the hours woked by employee 1: 8
##Enter the hours woked by employee 2: 10
##Enter the hours woked by employee 3: 12
##Enter the hours woked by employee 4: 14
##Enter the hours woked by employee 5: 25
##Enter the hours woked by employee 6: 30
##Enter the hourly pay rate: 15
##Gross pay for employee1: $120.00
##Gross pay for employee2: $150.00
##Gross pay for employee3: $180.00
##Gross pay for employee4: $210.00
##Gross pay for employee5: $375.00
##Gross pay for employee6: $450.00
##>>> 
