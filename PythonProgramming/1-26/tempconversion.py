#This pogram converts Celsius to Fahrenheit

#Input
cel = float( input( "Enter the temperature in Celcius: " ) )

#Calc/Pocessing
fah = cel * 9.0 / 5.0 + 32
fah2 = cel * 1.8 + 32
fah3 = cel * 9 / 5 + 32
fah4 = cel * (9.0 / 5.0) + 32

#Output
print( "Fahrenheit 1 is equal to", format( fah, '.2f' ), "degrees Fahrenheit" )
print( "Fahrenheit 2 is equal to", format( fah2, '.2f' ), "degrees Fahrenheit" )
print( "Fahrenheit 3 is equal to", format( fah3, '.2f' ), "degrees Fahrenheit" )
print( "Fahrenheit 4 is equal to", format( fah4, '.2f' ), "degrees Fahrenheit" )

##>>> 
##Enter the temperature in Celcius: 100
##Fahrenheit 1 is equal to 212.00 degrees Fahrenheit
##Fahrenheit 2 is equal to 212.00 degrees Fahrenheit
##Fahrenheit 3 is equal to 212.00 degrees Fahrenheit
##Fahrenheit 4 is equal to 212.00 degrees Fahrenheit
##>>> 
