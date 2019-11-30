#This program calculates test scores and averages for students in a class

#Input
STUDENTS = int( input( "How many students do you have? " ) )
TESTS = int( input( "How many test scores per student? " ) )

#Calc/Processing
for i in range( 0, STUDENTS ):
    print( "Student number", i + 1 )
    print( "-" * 16 )

    sum = 0
    avg = 0

    for j in range( 0, TESTS ):
        print( "Test number", j + 1, end = '' )
        score = float( input( ": " ) )
        sum += score
    avg = sum / TESTS
    print( "The average for Student number", i + 1, "is", format( avg, ".0f" ), "\n" )

##>>> 
##How many students do you have? 2
##How many test scores per student? 3
##Student number 1
##----------------
##Test number 1: 100
##Test number 2: 95
##Test number 3: 90
##The average for Student number 1 is 95 
##
##Student number 2
##----------------
##Test number 1: 81
##Test number 2: 82
##Test number 3: 80
##The average for Student number 2 is 81 
##
##>>> 
