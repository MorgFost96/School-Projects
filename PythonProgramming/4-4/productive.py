# Main Game File
#  - The file that allows the user to play the game

# Import Statements
import msvcrt
import random

# Global Variables
w = 79
h = 25
num_wilderness = 0
num_town = 0
wilderness = []
town = []

# Player
maxhp = 0
maxmp = 0
player = [ ]
armour = [ 0, 0, 0, 0, 0 ]
hands = [ 0, 0 ]

# Databases
id_list = [ "None",
            "Bronze Helmet",
            "Bronze Chainmail",
            "Bronze Leggings",
            "Bronze Gauntlets",
            "Bronze Boots",
            "Cloth Hat",
            "Cloth Robe",
            "Cloth Shirt",
            "Cloth Trousers",
            "Cloth Gloves",
            "Cloth Shoes",
            "Cloth Slippers",
            "Leather Helmet",
            "Leather Shirt",
            "Leather Pants",
            "Leather Gloves",
            "Bronze Sword",
            "Bronze Square Shield",
            "Wooden Staff",
            "Wooden Short Bow",
            "Bronze Dagger",
            "Walking Stick" ]

value_list = [ "0",
            "10",
            "3",
            "5",
            "3",
            "3",
            "2",
            "5",
            "3",
            "2",
            "1",
            "2",
            "1",
            "6",
            "3",
            "4",
            "2",
            "10",
            "10",
            "10",
            "10",
            "5",
            "1" ]

def box_title( s ):
    display = [ "#" * w,
                "#" + ( " " * ( w - 2 ) ) + "#",
                "#" + str.center( s, w - 2, " " ) + "#",
                "#" + ( " " * ( w - 2 ) ) + "#",
                "#" * w,
                "",
                "",
                "" ]
    return display

def menu_choice( display, options ):
    choice = 0
    num_choices = len( options )
    key = 0
    lines_remaining = h - ( len( display ) + len( options ) ) - 2

    
    while( key != 13 ):
        for line in display:
            print( str.center( line, w, " " ) )
        
        for line in options:
            if( line == options[ choice ] ):
                selected = "[ " + line + " ]"
                print( str.center( selected, w, " " ) )
            else:
                print( str.center( line, w, " " ) )

        print( "\n" * lines_remaining )
        key = ord( msvcrt.getch() )
        if( key == 72 ):    #Up Arrow
            choice -= 1
            if ( choice < 0 ):
                choice = num_choices - 1
        elif( key == 80 ):    #Down Arrow
            choice += 1
            if ( choice == num_choices ):
                choice = 0

    return choice

def menu_input( display, input_text ):
    lines_remaining = h - len( display ) - 3

    for line in display:
        print( str.center( line, w, " " ) )
        
    print( str.center( input_text, w, " " ) )

    print( "\n" * lines_remaining )
    player_input = input( ">>> " )

    return player_input

def main_menu( ):
    title = [ "",
              "",
              "",
              ".--.            .         .               .      ",
              "|   )           |        _|_   o       o _|_     ",
              "|--'.--..-.  .-.| .  . .-.|    ..    ._.  |  .  .",
              "|   |  (   )(   | |  |(   |    | \  /  |  |  |  |",
              "'   '   `-'  `-'`-`--`-`-'`-'-' `-`' -' `-`-'`--|",
              "                                                ;",
              "                                             `-' ",
              "",
              "",
              "", ]
    options = [ "New Game ", 
                "Load Game", 
                "Options  ",
                "Quit     " ]
    choice = menu_choice( title, options )
    if( choice == 0 ):
        character_creation()

def character_creation( ):
    character_display = box_title( "Character Creation" )
    name = menu_input( character_display, "Enter Your Name" )

    character_display.extend( [ "Choose Your Profession", "" ] )
    class_choice = [ "Fighter  ",
                     "Magician ",
                     "Ranger   ",
                     "Thief    ",
                     "Wanderer " ]
    job = menu_choice( character_display, class_choice )
    
    if( job == 0 ):    # Fighter
        armour[ 0 ] = id_list[ 1 ]
        armour[ 1 ] = id_list[ 2 ]
        armour[ 2 ] = id_list[ 3 ]
        armour[ 3 ] = id_list[ 4 ]
        armour[ 4 ] = id_list[ 5 ]
        
        character_display[ 8 ] = "Choose Your Class"
        focus_choice = [ "Knight   ",
                         "Paladin  ",
                         "Samurai  ",
                         "Barbarian" ]
        focus = menu_choice( character_display, focus_choice )
        
        if( focus == 0 ):    # Knight
            maxhp = 30
            maxmp = 5
            STR = 25
            INT = 0
            DEX = 10
            LUK = 5
            hands[ 0 ] = id_list[ 17 ]
            hands[ 1 ] = id_list[ 18 ]
    
    if( job == 1 ):    # Magician
        armour[ 0 ] = id_list[ 6 ]
        armour[ 1 ] = id_list[ 7 ]
        armour[ 2 ] = id_list[ 9 ]
        armour[ 3 ] = id_list[ 10 ]
        armour[ 4 ] = id_list[ 11 ]
        
        character_display[ 8 ] = "Choose Your Class"
        focus_choice = [ "Wizard      ",
                         "Cleric      ",
                         "Red Mage    ",
                         "Necromancer ",
                         "Elementalist" ]
        focus = menu_choice( character_display, focus_choice )
        
        if( focus == 0 ):    # Wizard
            maxhp = 10
            maxmp = 25
            STR = 0
            INT = 25
            DEX = 10
            LUK = 5
            hands[ 0 ] = id_list[ 19 ]
            hands[ 1 ] = id_list[ 0 ]

    player = [ name, maxhp, maxmp, STR, INT, DEX, LUK, 0 ]

    character_display[ 8 ] = "Name: " + player[ 0 ]
    character_display[ 9 ] = "Health: " + str( player[ 1 ] ) + " / " + str( maxhp )
    character_display.extend( [ "Mana: " + str( player[ 2 ] ) + " / " + str( maxmp ),
                                "Strength: " + str( player[ 3 ] ),
                                "Intelligence: " + str( player[ 4 ] ),
                                "Dexterity: " + str( player[ 5 ] ),
                                "Luck: " + str( player[ 6 ] ),
                                "",
                                "Left Hand: " + hands[ 0 ] + "        Right Hand: " + hands[ 1 ],
                                "",
                                "Confirm?" ] )

    confirm = menu_choice( character_display, [ "Yes", "No " ] )

    if( confirm == 0 ):
        enter_town( 0 )
    else:
        character_creation()

def enter_town( ):    
    town_display = box_title( Town )
    town_display.extend( [ "Enter the Town?" ] )
                     
    interact_choice = [ "Enter Town",
                        "Go to Wilderness" ]
    interact = menu_choice( town_display, interact_choice )
    
    if( interact == 0 ):
        town()
    elif( interact == 1 ):
        wilderness()

def wilderness( ):
    global num_town
    global num_wilderness
    
    grass = False
    
    cols = random.randrange( 10, 50 )
    rows = random.randrange( 10, 50 )
    wilderness = [ [ " " for c in range( cols ) ] for r in range( rows ) ]

    for r in range( len( wilderness ) ):
        for c in range( len( wilderness[ 0 ] ) ):
            random = random.randint( 1, 1000 )

            if( random <= 100 ):
                wilderness[ r ][ c ] = "G"
            elif( random <= 150 ):
                wilderness[ r ][ c ] = "E"
    
    wilderness[ random.randrange( 0, rows ), random.randrange( 0, cols ) ] = "C"

    pos = [ random.randrange( 0, rows ), random.randrange( 0, cols ) ]
    wilderness[ pos[ 0 ] ][ pos[ 1 ] ] = "T"

    w_display = box_title( "Wilderness" )
    w_display.extend( [  ] )
    
    

def index( ):
    i = 0
    print( "Item List: " )
    while( i < len( id_list ) ):
        print( i, ":\t", value_list[ i ], "\t", id_list[ i ], sep = "" )
        i += 1

def main( ):
    main_menu()

main()

##Item List: 
##0:	0	None
##1:	10	Bronze Helmet
##2:	3	Bronze Chainmail
##3:	5	Bronze Leggings
##4:	3	Bronze Gauntlets
##5:	3	Bronze Boots
##6:	2	Cloth Hat
##7:	5	Cloth Robe
##8:	3	Cloth Shirt
##9:	2	Cloth Trousers
##10:	1	Cloth Gloves
##11:	2	Cloth Shoes
##12:	1	Cloth Slippers
##13:	6	Leather Helmet
##14:	3	Leather Shirt
##15:	4	Leather Pants
##16:	2	Leather Gloves
##17:	10	Bronze Sword
##18:	10	Bronze Square Shield
##19:	10	Wooden Staff
##20:	10	Wooden Short Bow
##21:	5	Bronze Dagger
##22:	1	Walking Stick
