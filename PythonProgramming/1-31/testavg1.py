#This calculates the grade using the average of three test scores

#Input
t1 = float( input( "Enter the first test score: " ) )
t2 = float( input( "Enter the second test score: " ) )
t3 = float( input( "Enter the third test score: " ) )

#Calc/Pocessing
sum = t1 + t2 + t3
avg = sum / 3
print ( "The average is ", avg )



#Output
if 90 <= avg <= 100:
    print('A')
if 80 <= avg <= 89:
    print('B')
if 70 <= avg <= 79:
    print('C')
if avg <= 69:
    print('D')
if avg > 100:
    grade = 'greater than 100'
if avg < 0:
    grade = 'less than 0'

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
