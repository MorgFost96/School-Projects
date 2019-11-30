# Tuples
#  - An immutable sequence ( contents cannot be changed )

ring_tuple = ( 1, 2, 3, 4, 5 )
print( ring_tuple )
# >>> ( 1, 2, 3, 4, 5 )

names = ( "Holly", "Warren", "Ashley" )
for n in names:
    print( n )
# >>> Holly\nWarren\nAshley

#
# Tuples Support Indexing
#
for i in range( len( names ) ):
    print( names[ i ] )
# >>> Holly\nWarren\nAshley

#
# Creating a Tuple with One Element
#
my_tuple = ( 1, )
wrong_tuple = ( 1 )
print( my_tuple )
print( wrong_tuple )
# >>> ( 1 )    # my_tuple is correct
# >>> 1        # wrong_tuple is incorrect

#
# Why Use Tuples?
#  - Process Faster
#  - Good for Lots of Data
#  - Supports all list operations except
#     - Append, Remove, Insert, Reverse, Sort

#
# Convert List to Tuple and Vice Versa
#
tuple_to_list = ( 1, 2, 3 )
list_from_tuple = list( tuple_to_list )
print( tuple_to_list )
print( list_from_tuple )
# >>> ( 1, 2, 3 )
# >>> [ 1, 2, 3 ]

