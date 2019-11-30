#Morgan Foster
#1021803
# Homework 5

class Loan:
    def __init__( self, interest, years, amt, name ):
        self.__interest = interest
        self.__years = years
        self.__amt = amt
        self.__name = name

    def getInterest( self ):
        return self.__interest

    def getYears( self ):
        return self.__years

    def getAmt( self ):
        return self.__amt

    def getName( self ):
        return self.__name
    
    def setInterest( self, interest ):
        self.__interest = interest

    def setYears( self, years ):
        self.__years = years

    def setAmt( self, amt ):
        self.__amt = amt

    def setName( self, name ):
        self.__name = name

    def getMonthlyPayment( self ):
        return self.__amt * self.__interest / ( 1 - ( 1 / ( 1 + self.__interest ) ** ( self.__years * 12 ) ) )

    def getTotalPayment( self ):
        return self.getMonthlyPayment() * self.__years * 12

def main():
    interest = float( input( "Enter yearly interest rate, for example, 7.25: " ) )
    years = int( input( "Enter number of years as an integer: " ) )
    amt = float( input( "Enter loan amount, for example, 120000.95: " ) )
    name = input( "Enter a borrower's name: " )
    loan = Loan( interest, years, amt, name )

    print( "The loan is for", loan.getName() )        
    print( "The monthly payment is", format( loan.getMonthlyPayment(), "0.2f" ) )
    print( "The total payment is", format( loan.getTotalPayment(), "0.2f" ) )
    print( "" )
    
    response = input( "Do you want to change the loan amount? Y for yes or enter to quit " )
    if( response.lower() == 'y' ):
        amt = float( input( "Enter new loan amount " ) )
        loan.setAmt( amt )
        
        print( "The loan is for", loan.getName() )        
        print( "The monthly payment is", format( loan.getMonthlyPayment(), "0.2f" ) )
        print( "The total payment is", format( loan.getTotalPayment(), "0.2f" ) )
        
main()

##>>> 
##Enter yearly interest rate, for example, 7.25: 2.5
##Enter number of years as an integer: 5
##Enter loan amount, for example, 120000.95: 1000.00
##Enter a borrower's name: John Jones
##The loan is for John Jones
##The monthly payment is 2500.00
##The total payment is 150000.00
##
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 5000
##The loan is for John Jones
##The monthly payment is 12500.00
##The total payment is 750000.00
##>>> 

    
