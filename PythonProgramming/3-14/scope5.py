#Variable Scope Example

x = 1

def incr():
    global x
    x = x + 1
    print( x )

incr()
print( x )

##>>>
##2
##2
##>>> 
