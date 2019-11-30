#Rock Paper Scissors

#Imports
import random

#Input
points = 0
npcpoints = 0

#Calc/Processing
while( points < 2 and npcpoints < 2 ):
    choice = int( input( "Rock, Paper, Scissors [0, 1, 2]: " ) )
    npcchoice = random.randint( 0, 2 )
    if( choice == 0 ):
        print( "You chose Rock" )
        if( npcchoice == 1 ):
            npcpoints += 1
            print( "The Computer chose Paper" )
            print( "You Lost\n" )
        elif( npcchoice == 2 ):
            points += 1
            print( "The Computer chose Scissors" )
            print( "You Won\n" )
        else:
            print( "The Computer chose Rock" )
            print( "You Tied\n" )
    elif( choice == 1 ):
        print( "You chose Paper" )
        if( npcchoice == 2 ):
            npcpoints += 1
            print( "The Computer chose Scissors" )
            print( "You Lost\n" )
        elif( npcchoice == 0 ):
            points += 1
            print( "The Computer chose Rock" )
            print( "You Won\n" )
        else:
            print( "The Computer chose Paper" )
            print( "You Tied\n" )
    elif( choice == 2 ):
        print( "You chose Scissors" )
        if( npcchoice == 0 ):
            npcpoints += 1
            print( "The Computer chose Rock" )
            print( "You Lost\n" )
        elif( npcchoice == 1 ):
            points += 1
            print( "The Computer chose Paper" )
            print( "You Won\n" )
        else:
            print( "The Computer chose Scissors" )
            print( "You Tied\n" )
    else:
        print( "Invalid Input\n" )

#Output
if( points >= 2 ):
    print( "You Win!" )
else:
    print( "You Lose!" )

##>>> 
##Rock, Paper, Scissors [0, 1, 2]: 0
##You chose Rock
##The Computer chose Paper
##You Lost
##
##Rock, Paper, Scissors [0, 1, 2]: 1
##You chose Paper
##The Computer chose Paper
##You Tied
##
##Rock, Paper, Scissors [0, 1, 2]: 2
##You chose Scissors
##The Computer chose Scissors
##You Tied
##
##Rock, Paper, Scissors [0, 1, 2]: 3
##Invalid Input
##
##Rock, Paper, Scissors [0, 1, 2]: 0
##You chose Rock
##The Computer chose Scissors
##You Won
##
##Rock, Paper, Scissors [0, 1, 2]: 1
##You chose Paper
##The Computer chose Rock
##You Won
##
##You Win!
##>>> 
