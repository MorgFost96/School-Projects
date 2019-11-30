#Morgan Foster
#1021803
#This program guesses your number between 0 and 1000

#Input
fav = int( input( "What is your favorite number? ") )
print( "\nThink of a different number between 0 and 1000" )

#Calc/Processing
max = 1000
min = 0
guess = 0

if fav < 0:
    fav = -fav
rand = (fav * 13 + 17) % 100   

if ( rand % 2 == 0 ):
    rand = 500 - rand
else:
    rand = 500 + rand

print("Is your number ", rand, "?", sep = '')
response = input( "Type 'y' or 'n': " )
tries = 1

#Output
if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    


if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( response == 'y' and guess == 0):
    print("\n\nYour number was ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
    guess = 1
elif ( response == 'n' and guess == 0):
    tries += 1
    print("Is your number larger than ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )
    if ( response == 'y' ):
        min = rand
        rand = int( ( rand + max ) / 2 ) + 1
    else:
        max = rand
        rand = int( ( rand + min ) / 2 )
    print("\nIs your number ", rand, "?", sep = '')
    response = input( "Type 'y' or 'n': " )



if ( guess == 0 ):
    print("\n\nYour number is ", rand, "! I guessed it in ", tries, " tries!",\
          sep = '')
