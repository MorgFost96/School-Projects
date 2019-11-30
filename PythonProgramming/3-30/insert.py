#This program demonstrates the insert method

def main():
    names = [ "James", "Kathryn", "Bill" ]

    print( "The list before the insert: " )
    print( names )

    names.insert( 0, "Joe" )

    print( "The list fter the insert: " )
    print( names )

main()

##>>> 
##The list before the insert: 
##['James', 'Kathryn', 'Bill']
##The list fter the insert: 
##['Joe', 'James', 'Kathryn', 'Bill']
##>>> 
