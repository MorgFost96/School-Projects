#Morgan Foster
#1021803
#
# Exam 3 Review Notes

#-------------
# Test Review
#-------------

#  - Focus on Strings and Functions
#     - Definition of func
#        - A function is a group of statements that exists within a program for
#          the purpose of performing a specific task
#     - Benefits of func
#        - Simpler Code
#           - Break down into individual or smaller tasks
#        - Reusable
#        - Better Testing
#           - Easy to isolate and fix
#        - Faster Development
#           - Each programmer can write different functions and put them together

#  - Global/Local Variables
#     - Global: Can be accessed anywhere in the program
#     - Local: Can only be accessed where it is declared
#     - Don't use global variables because of side effects

#  - Arguments/Parameters: Pass information

#  - Keyword/Positional
#     - Pos pos key pos doesn't work
def fn (a, b, c = 1):
    return a * b + c

print fn (1, 2)                # returns 3, positional and default.
print fn (1, 2, 3)             # returns 5, positional.
print fn (c = 5, b = 2, a = 2) # returns 9, named.
print fn (b = 2, a = 2)        # returns 5, named and default.
print fn (5, c = 2, b = 1)     # returns 7, positional and named.
print fn (8, b = 0)            # returns 1, positional, named and default.

