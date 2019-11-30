#This pogram demonstrates how o get the
#index of an item in a list then removes
#that item

def main():
    food = [ "Pizza", "Burgers", "Chips" ]

    print( "Here are the items in the food list: " )
    print( food )

    item = input( "Which item would you like to remove? " )

    try:
        food.remove( item )
        print( "Here is the revised list: " )
        print( food )
    except ValueError:
        print( "That item was not found in the list" )

main()

##>>> 
##Here are the items in the food list: 
##['Pizza', 'Burgers', 'Chips']
##Which item shoud I change? Chips
##Enter the new value: Buffalo Wings
##Here is the revised list: 
##['Pizza', 'Burgers', 'Buffalo Wings']
##>>> 
