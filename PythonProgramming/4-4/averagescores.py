# Prints the average test score with the lowest dropped

def get_scores():
    test_scores = []
    again = "y"
    
    while( again.upper() == "Y" ):
        value = float( input( "Enter test score: " ) )
        test_scores.append( value )
        print( "Do you want to add another?" )
        again = input( "y = yes, anything = no " )
        print()

    return test_scores

def get_totals( value_list ):
    total = 0.0
    
    for num in value_list:
        total += num
    return total

def main():
    scores = get_scores()
    total = get_totals( scores )
    lowest = min( scores )
    average = ( total - lowest ) / ( len( scores ) - 1)
    print( "Average:", average )
        
main()
