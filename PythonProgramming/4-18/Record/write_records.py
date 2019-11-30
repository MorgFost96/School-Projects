# Records
#  - A record is a complete set of data about an item and a field is an
#    individual piece of data within a record
#
# Writes the records for employees.txt onto the hard drive

def main():
    num_emps = int( input( "How many employee records? " ) )
    
    emp_file = open( "employees.txt", "w" )

    for count in range( 1,num_emps + 1 ):
        print( "" )
        print( "Enter data for employee #", count, sep = "" )
        name = input( "Name: " )
        id_num = input( "ID: " )
        dept = input( "Department: " )
        
        emp_file.write( name + "\n" )
        emp_file.write( id_num + "\n" )
        emp_file.write( dept + "\n" )

    emp_file.close()

    print( "" )
    print( "Employee records written to file" )

main()

##>>>
##How many employee records? 3
##
##Enter data for employee #1
##Name: Ace
##ID: 1
##Department: IVC
##
##Enter data for employee #2
##Name: Morgan
##ID: 2
##Department: IVC
##
##Enter data for employee #3
##Name: Loke
##ID: 10
##Department: IVC
##
##Employee records written to file
##>>> 
