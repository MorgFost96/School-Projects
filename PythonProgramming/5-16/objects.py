#Morgan Foster
#1021803
# Intro to Object Oriented Programming ( OOP )
# - OOP enables you to develop large scale software and GUI effectively
# - A class defines the properties and behaviors for objects
# - Objects are created from classes

# Imports
import math

# ---
# OOP
# ---
# - Use of objects to create programs
# - Object is a software entity that contains both data and code
# - The procedure ( codes ) that an object performs are called methods
# - Encapsulation
#    - Combining of data and code into a single object
# - An object typically hides its data ( data binding ) but allows outside code to access its methods
# - Code reusability

# --------------------------------------
# Differences between Procedural and OOP
# --------------------------------------
# Procedural
# - Separation of data and codes
# - If change way of storing data from variables to list, must modify all functions to accept list
#
# OOP
# - Data and codes all encapsulated in class
# - Just change the data and methods in class and all objects will take care of themselves

class IncorrectCircle:
    # Initializer or constructior
    # - Automatically called when object is instantiated
    def __init__( self, radius = 1 ):
        self.radius = radius

    # Self Parameter that refers to the object that invokes the method
    def getPerimeter( self ):
        return 2 * self.radius * math.pi

    # Can use name other than self
    # - Self is conventional
    def getArea( you ):
        return you.radius ** 2 * math.pi

    def setRadius( self, radius ):
        self.radius = radius

class Circle:
    # Place .__ prevents direct access to the data member
    def __init__( self, radius = 1 ):
        self.__radius = radius

    # Getters or Accessors
    def getRadius( self ):
        return self.__radius
    
    def getPerimeter( self ):
        return 2 * self.__radius * math.pi

    def getArea( you ):
        return you.__radius ** 2 * math.pi

    # Setter or Mutator
    def setRadius( self, radius ):
        self.__radius = radius

def test():
    incorrect_circle = IncorrectCircle()
    # circle.radius is called a dot access
    print( "The area of the circle of radius", incorrect_circle.radius, "is", incorrect_circle.getArea() )

    circle = Circle( 25 )
    print( "The area of the circle of radius", circle.getRadius(), "is", circle.getArea() )

    # 
    # Direct access to data member
    incorrect_circle.radius = 100
    # circle.radius = 100 won't work

    
    # Change the radius from 25 to 100
    circle.setRadius( 100 )
    print( incorrect_circle.radius )
    print( circle.getRadius() )

test()

# To Instantiate is to create an instance of an object
