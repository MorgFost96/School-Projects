#List Examples

#----------------
#Lists of Numbers
#----------------
even_num = [ 2, 4, 6, 8, 10 ]

#----------------
#Lists of Strings
#----------------
name = [ "Molly", "Steven", "Will" ]

#-------------------------
#Mixed Strings and Numbers
#-------------------------
info = [ "Alicia", 27, 155 ]

#------------
#Print a List
#------------
num = [5, 10, 15, 20 ]
print( num )
#>>>[ 5, 10, 15, 20 ]

#---------------
#List() Function
#---------------
num_list = ( range( 5 ) )
print( num_list )
#>>>[ 0, 1, 2, 3, 4 ]


#-----------------
#Lists are Mutable
#-----------------
mut = [ 1, 2, 3, 4, 5 ]
#>>>[ 1, 2, 3, 4, 5 ]

mut[ 0 ] = [ 99 ]
#>>>[ 99, 2, 3, 4, 5 ]

#---------------------------------
#Fill a List of Values using Index
# - Create List First
# - Fill the List
#---------------------------------
fill = [ 0 ] * 5
print( fill )
#>>>[ 0, 0, 0, 0, 0 ]

index = 0
while index < len( fill ):
    fill[ index ] = 99
    index += 1
print( fill )
#>>>[ 99, 99, 99, 99, 99 ]

#-------------------
#Concatenating Lists
#-------------------
list1 = [ 1, 2, 3, 4 ]
list2 = [ 5, 6, 7, 8 ]
list3 = [ "Jim", "Jon" ]

list4 = list1 + list2
print( list4 )
#>>>[ 1, 2, 3, 4, 5, 6, 7, 8 ]

list5 = list1 + list3
print( list5 )
#>>>[ 1, 2, 3, 4, "Jim", "Jon" ]

#------------
#List Slicing
#------------
days = [ "Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat" ]
mid_days = days[ 2:5 ]
print( mid_days )
#>>>[ "Tues", "Wed", "Thurs" ]

print( days[:3] )
#>>>[ "Sun", "Mon", "Tues" ]

print( days[2:] )
#>>>[ "Tues", "Wed", "Thurs", "Fri", "Sat" ]

print( days[ : ] )
#>>>[ "Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat" ]

#-----------
#In Operator
#-----------

def main():
    prod_name = [ "V4", "F8", "Q1", "R6" ]
    search = input( "Enter a product name: " )
    if search in prod_name:
        print( search, "was found in list" )
    else:
        print( search, "not found" )

#------------
#List Methods
#------------
#
#append( item )
# - Adds items to the end of a list
#
#index( item )
# - Returns the index of the element whose value equals
#   the item. A ValueError exception is raised if the
#   item is not found
#
#insert( index, item )
# - Inserts the item into the list at the specified index
#
#sort()
# - Sots the items in ascending order
#
#remove( item )
# - Removes the first occurance of the iem from he list.
#   ValueError raised if the item is not found
#
#revese()
# - Reverses the order of the items in a list

#-----------
#Sort Method
#-----------
sorted_list = [ 9, 1, 0, 2, 8 ]
sorted_list.sort()
print( sorted_list )
#>>> [ 0, 1, 2, 8, 9 ]
sorted_list.reverse()
print( sorted_list )
#>>> [ 9, 8, 2, 1, 0 ]

#----------------
#Min Max Function
#----------------
minmax = [ 5, 4, 3, 2, 50, 40, 30 ]
print( max( minmax ) )
#>>> 50
print( min( minmax ) )
#>>> 2

#-------------------------
#Use Functions with a List
#-------------------------
def listfunc1():
    num = [ 2, 4, 6, 8, 10 ]
    print( "The total is", get_total( num ) )

def get_total( value_list ):
    total = 0
    for num in value_list:
        total += num
    return total

def listfunc2():
    num = get_values()
    print( "The numbers in the list are: ")
    print( numbers )

def get_values():
    values = []
    again = "Y"
    while again.upper() == "Y":
        num = int( input( "Enter a number: " ) )
        values.append( num )
        print( "Do you want to add another number?" )
        again = input( "'Y' for yes" )
        print()
    return values

#--------------
#Copying a List
#--------------
copy1 = [ 1, 2, 3, 4 ]
copy2 = copy1
print( copy1 )
#>>> [ 1, 2, 3, 4 ]
print( copy2 )
#>>> [ 1, 2, 3, 4 ]
copy1[0] = 99
print( copy1 )
#>>> [ 99, 2, 3, 4 ]
print( copy2 )
#>>> [ 1, 2, 3, 4 ]


    
    
