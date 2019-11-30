#This calculates the grade using the average of three test scores

#Input
t1 = float( input( "Enter the first test score: " ) )
t2 = float( input( "Enter the second test score: " ) )
t3 = float( input( "Enter the third test score: " ) )

#Calc/Pocessing
sum = t1 + t2 + t3
avg = sum / 3

if avg < 0 or avg > 100:
    grade = 'Invalid'
else:
    if avg >= 90 and avg <= 100:
        grade = 'A'
    else:
        if avg >= 80 and avg <= 89:
            grade = 'B'
        else:
            if avg >= 70 and avg <= 79:
                grade = 'C'
            else:
                grade = 'F'

#Output
print( "The average test score is", format( avg, '0.2f' ),\
       "and the final grade is", grade )

##>>> 
##Enter the first test score: 90
##Enter the second test score: 95
##Enter the third test score: 100
##The average test score is 95.00 and the final grade is A
##>>> 
##Enter the first test score: 80
##Enter the second test score: 85
##Enter the third test score: 90
##The average test score is 85.00 and the final grade is B
##>>> 
##Enter the first test score: 70
##Enter the second test score: 75
##Enter the third test score: 80
##The average test score is 75.00 and the final grade is C
##>>> 
##Enter the first test score: 60
##Enter the second test score: 65
##Enter the third test score: 70
##The average test score is 65.00 and the final grade is F
##>>> 
##Enter the first test score: -10
##Enter the second test score: -20
##Enter the third test score: -30
##The average test score is -20.00 and the final grade is Invalid
##>>> 
##Enter the first test score: 110
##Enter the second test score: 120
##Enter the third test score: 130
##The average test score is 120.00 and the final grade is Invalid
##>>> 
