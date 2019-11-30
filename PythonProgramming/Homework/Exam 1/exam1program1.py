#Morgan Foster
#1021803
#This program calculates the gravitational force using the mass of a person

#Input
m = float( input("Enter Mr. Jones' Weight: ") )

#Calc/Processing
r = 6378 * 10 ** 3
m1 = 5.9742 * 10 ** 24
G = 6.67300 * 10 ** -11

F = G * m1 * m / r ** 2
g = F / m

#Output
print( "The resulting value of g is", format(g, '0.4f'),\
       "which is close to the earth's gravitational force." )

##>>> 
##Enter Mr. Jones' Weight: 68.0389
##The resulting value of g is 9.8001 which is close to the earth's gravitational force.
##>>> 
