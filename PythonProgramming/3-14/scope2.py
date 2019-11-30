#Variable Scope Example

x = 1

def f1():
    x = 2
    print( x )

f1()
print( x )
    
##>>> 
##2
##1
##>>> 
