# Recursion
#  - A function that calls itself

# ---------
# Iterative
# ---------
# Main -> a -> b -> c -> d

# ---------
# Recursive
# ---------
# Main -> a -> a -> a -> a

# ----
# Note
# ----
# Whenever possible, use iterave over recusive
# Why? Faster and uses less memory

# -------
# Example
# -------
def main():
    message()

def message():
    print( "This is a recursive function" )

# ---------
# Factorial
# ---------
# 4! = 4 * 3 * 2 * 1
# 3! =     3 * 2 * 1
# 2! =         2 * 1
# 1! =             1
# 0! =             1

def fact( n ):
    if n == 0:
        return 1
    else:
        return n * fact( n - 1 )

def run_fact():
    n = int( input( "Enter Non Negative Number: " ) )
    f = fact( n )
    print( "The factorial of n is", f )

run_fact()

# -----------
# Exponential
# -----------

def two():
    if n == 0:
        return 1
    else:
        return 2 * two( n - 1 )

def run_two():
    n = int( input( "Enter Non Negative Number: " ) )
    t = two( n )
    pritn( "Two to the power of", n, "is", t )

run_two()

# ---------
# Fibonacci
# ---------

def fib( n ):
    if( n == 1 or n == 2 ):
        return 1
    else:
        return fib( n - 1 ) + fib( n - 2 )

def run_fib():
    n = int( input( "Fibonacci Position: " ) )
    f = fib( n )
    print( "The value is", f )

run_fib()


