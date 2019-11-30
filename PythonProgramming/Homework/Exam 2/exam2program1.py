#Morgan Foster
#1021803
#This program generates a two digit number has the user input a two digit number. The program rewards the user
#if the user's guess is close to the randomly generated number.

#Imports
import random

#Input
money = 0
randomNum = random.randint( 10, 99 )

userNum = int( input( "Enter a Two-Digit Number: " ) )
while( userNum < 10 or userNum > 99 ):
    print( "Invalid Number" )
    userNum = int( input( "Enter a Two-Digit Number: " ) )

#Calc/Processing
randomNumA = randomNum // 10
randomNumB = randomNum % 10

userNumA = userNum // 10
userNumB = userNum % 10


if( userNum == randomNum ):
    money += 10000
elif( userNumA == randomNumB and userNumB == randomNumA ):
    money += 3000
elif( userNumA == randomNumA or userNumB == randomNumB or userNumA == randomNumB or usernumB == randomNumA ):
    money += 1000

#Output
print( "" )
print( "Your Number:", userNum )
print( "Randomly Generated Number:", randomNum )
print( "Money: $", format( money, ",.2f" ), sep = "" )

##>>> 
##==== RESTART: D:\School\2016 - 17\Python\Homework\Exam 2\exam2program1.py ====
##Enter a Two-Digit Number: 12
##
##Your Number: 12
##Randomly Generated Number: 12
##Money: $10,000.00
##>>>
##==== RESTART: D:\School\2016 - 17\Python\Homework\Exam 2\exam2program1.py ====
##Enter a Two-Digit Number: 12
##
##Your Number: 12
##Randomly Generated Number: 21
##Money: $3,000.00
##>>> 
##==== RESTART: D:\School\2016 - 17\Python\Homework\Exam 2\exam2program1.py ====
##Enter a Two-Digit Number: 12
##
##Your Number: 12
##Randomly Generated Number: 91
##Money: $1,000.00
##>>> 
##==== RESTART: D:\School\2016 - 17\Python\Homework\Exam 2\exam2program1.py ====
##Enter a Two-Digit Number: 12
##
##Your Number: 12
##Randomly Generated Number: 32
##Money: $1,000.00
##>>> 
