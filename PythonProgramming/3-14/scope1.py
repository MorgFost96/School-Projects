#Variable Scope Example

globalVar = 1

def f1():
    localVar = 2
    print( globalVar )
    print( localVar )

#Function Calls
print( globalVar )
f1()
#print( localVar )      #Not Defined

##>>> 
##1
##1
##2
##>>> 
