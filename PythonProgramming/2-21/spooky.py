#This program does spooky games
import random

#Input
points = 0
num = random.randint( 1, 3 )


#Calc/Processing
print( "INSTRUCTIONS" )
print( "There are 3 doors in front of you" )
print( "A ghost is behind one of the doors" )
print( "He will change his position after every choice" )
print( "You gain one point if you choose a door without a ghost" )
print( "You lose once you choose the door that the ghost is behind\n\n" )

choice = int( input("Which door would you like to choose [1, 2, 3]: ") )

while choice != num:
    if( choice < 1 or choice > 3 ):
        print( "Invalid Input\n" )
        choice = int( input("Which door would you like to choose [1, 2, 3]: ") )
    else:
        print( "The ghost was not behind that door, you earned a point\n" )
        points += 1
        num = random.randint( 1, 3 )
        choice = int( input("Which door would you like to choose [1, 2, 3]: ") )
        
#Output
print( "\nGhost!" )
print( "Go away" )
print( "Game Over, you score", points )

##>>> 
##INSTRUCTIONS
##There are 3 doors in front of you
##A ghost is behind one of the doors
##He will change his position after every choice
##You gain one point if you choose a door without a ghost
##You lose once you choose the door that the ghost is behind
##
##
##Which door would you like to choose [1, 2, 3]: 0
##Invalid Input
##
##Which door would you like to choose [1, 2, 3]: 1
##The ghost was not behind that door, you earned a point
##
##Which door would you like to choose [1, 2, 3]: 2
##The ghost was not behind that door, you earned a point
##
##Which door would you like to choose [1, 2, 3]: 3
##The ghost was not behind that door, you earned a point
##
##Which door would you like to choose [1, 2, 3]: 1
##The ghost was not behind that door, you earned a point
##
##Which door would you like to choose [1, 2, 3]: 2
##The ghost was not behind that door, you earned a point
##
##Which door would you like to choose [1, 2, 3]: 3
##
##Ghost!
##Go away
##Game Over, you score 5
##>>> 
