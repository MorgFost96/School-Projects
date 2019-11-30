# Sets
#  - Lists for storing a collection of elements. Unlike lists, the elements
#    in a set are non-duplicates and are not placed in any order.
#  - Use sets when order of elements are not imported because it is
#    more efficient
#  - Sets are mutable

# Create set using set function
s1 = set()

# Create set with 3 elements
s2 = { 1, 3, 5 }

# From c list
s3 = set( [ 1, 3, 5 ] )

# Create tuple and list from sets
# k = list( set )
# t = tuple( set )

# No duplicates
s4 = set( "abac" )
# >>> { 'a', 'b', 'c' }

# Errors
# my_set = set( "one", "two", "three" )
#  - Not allowed because the set function accepts only one argument
# my_set = set( "one two three" )
# >>> { 'o', 'n', 'e', ' ', 't', 'w', 'h', 'r' }
my_set = set( [ "one", "two", "three" ] )

a_set = { 'a', 'b', 'c', 'd' }
b_set = { 'c', 'd', 'e', 'f' }

# Intersection &
a_set & b_set
# >>> { 'c', 'd' }

# Union |
a_set | b_set
# >>> { 'a', 'b', 'c', 'd', 'e', 'f' }

# Difference
a_set - b_set
# >>> { 'a', 'b' }
b-set - a_set
# >>> { 'e', 'f' }

# Symmetric Difference ^
a_set ^ b_set
# >>> { 'a', 'b', 'e', 'f' }
b_set ^ a_set
# >>> { 'a', 'b', 'e', 'f' }

# Superset/Subset
small_set = { 'a', 'b', 'c' }
big_set = set( "abcdef" )
small_set <= bigset
# >>> True
big_set <= big_set
# >>> True
small_set >= big_set
# >>> False

