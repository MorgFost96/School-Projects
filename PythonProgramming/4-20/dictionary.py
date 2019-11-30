# Dictionary
#  - An objet that stores a collection of data.
#  - Each element has two parts:
#     - Key
#     - Value
#  - The key is used to locate a specific value

# ------------------
# English Dictionary
# ------------------
#  - The word = Key
#  - Definition = Value
#
#  - emp_ID = Key
#  - emp_name = Value

# -------------------
# Creating Dictionary
# -------------------
#  - { key : value }
phonebook = { "Chris" : "555-1111",
              "Kate" : "555-2222",
              "John" : "555-3333" }

# ----
# Keys
# ----
#  - Immutable
#  - Int, String, or Tuple

# ------
# Values
# ------
#  - Anything
#  - Mutable

# ----------
# Dictionary
# ----------
#  - Mutable

# ---------------
# Retrieve Values
# ---------------
print( phonebook )
# >>> { 'Chris' : '555-1111', 'John' : '555-3333', 'Kate' : '555-2222' }
#  - Order Changes
#  - Cannot use index
#     - Must use key to retrieve information

print( phonebook[ "Chris" ] )
# >>> "555-1111"
#  - Keys are Case Sensitive

# ---------------------
# In or Not In Operator
# ---------------------
if "Chris" in phonebook:
    print( phonebook[ "Chris" ] )
elif "Chris" not in phonebook:
    print( "'Chris' was not found in 'phonebook'" )

# --------------------------
# Add Elements to Dictionary
# --------------------------
# - Cannot have duplicate keys
phonebook[ "Joe" ] = "555-4444"
print( phonebook )
# >>> { 'Chris' : '555-1111', 'John' : '555-3333', 'Kate' : '555-2222', 'Joe' : '555-4444' }
phonebook[ "Chris" ] = "555-0123"
print( phonebook )
# >>> { 'Chris' : '555-0123', 'John' : '555-3333', 'Kate' : '555-2222', 'Joe' : '555-4444' }

# -----------------
# Deleting Elements
# -----------------
#  - If the key is found, it will be removed
#  - Otherwise there will be a KeyError Exception raised
del phonebook[ 'Chris' ]
print( phonebook )
# >>> { 'John' : '555-3333', 'Kate' : '555-2222', 'Joe' : '555-4444' }

# ------
# Length
# ------
num_items = len( phonebook )
print( num_items )
# >>> 3

# -----------------
# Mixing Data Types
# -----------------
test_scores = { "Kay" : [ 100, 88, 92, 89 ],
                "Luis" : [ 35, 37, 45, 57 ],
                "Sophia" : [ 85, 93, 83, 58 ],
                "Ethan" : [ 99, 98, 90, 100 ] }

print( test_scores[ "Sophia" ] )
# >>> [ 85, 93, 83, 58 ]

# ----------------------------
# Creating an Empty Dictionary
# ----------------------------
empty = {}

# -----
# Loops
# -----
for key in phonebook:
    print( key )
# >>> John
#     Kate
#     Joe
for key in phonebook:
    print( key, phonebook[ key ] )
# >>> John 555-3333
#     Kate 555-2222
#     Joe 555-4444

# -------
# Methods
# -------
#  - clear()
#     - Clears all elements in a dictionary
#     - Ex. phonebook.clear()
#           print( phonebook )
#           >>> {}
#  - get()
#     - Ex. value = phonebook.get( 'Kate', 'Entry not Found' )
#           print( value )
#           >>> 555-2222
#  - keys()
#     - Ex. for key in phonebook.keys():
#               print( key )
#           >>> John
#               Kate
#               Joe
#  - pop()
#     - Returns value with specified key then removes the key-value
#       pair from the dictionary
#     - Ex. phone_num = phonebook.pop( "John", "Entry not Found" )
#           print( phone_num )
#           >>> '555 - 1111'
#        - John is no longer in the dictionary
#  - popitem()
#     - Returns randomly selected key-value pair then removes the
#       key-value pair from the dictionary
#     - Returns a tuple of ( key value ) if assigned to one variable 
#     - Ex. key, value = phonebook.popitem()
#           print( key, vallue )
#           >>> John 555-3333
#     - Ex. key = phonebook.popitem()
#           print( key )
#           >>> ( 'John', '555-3333' )
#  - values()
#     - Returns the values
#     - Ex. for val in phonebook.values():
#               print( val )
#           >>> 555-3333
#               555-2222
#               555-4444

