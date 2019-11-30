#This program calculates the sum and average of 3 numbers

#input
name=input("Enter your name ")
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
num3=int(input("Enter the third number "))

#calc/processing
sum=num1+num2+num3
avg=sum/3

#output
print("Your name is", name)
print("The sum is", sum)
print("The average is", avg)

##>>> 
##Enter your name Johnny Five
##Enter the first number 10
##Enter the second number 20
##Enter the third number 30
##Traceback (most recent call last):
##  File "C:\Users\alowder1\Desktop\sumavg2.py", line 12, in <module>
##    sum=a+b+c
##NameError: name 'a' is not defined
##>>> 
##Enter your name Johnny Five
##Enter the first number 10
##Enter the second number 20
##Enter the third number 30
##Your name is Johnny Five
##The sum is 60
##The average is 20.0
##>>> 
