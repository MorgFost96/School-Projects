#List Examples

#----------------
#Lists of Numbers
#----------------
even_num = [ 2, 4, 6, 8, 10 ]

#----------------
#Lists of Strings
#----------------
name[ "Molly", "Steven", "Will" ]

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
num_list( range( 5 ) )
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

print( : ] )
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
