# Reads the records from employees.txt

def main():
    emp_file = open( "employees.txt", "r" )
    name = emp_file.readline()
    while name != "":
        id_num = emp_file.readline()
        dept = emp_file.readline()
        
        name = name.rstrip( "\n" )
        id_num = id_num.rstrip( "\n" )
        dept = dept.rstrip( "\n" )

        print( "" )
        print( "Name:", name )
        print( "ID:", id_num )
        print( "Department:", dept )

        name = emp_file.readline()

    emp_file.close()

main()

##>>> 
##
##Name: Ace
##ID: 1
##Department: IVC
##
##Name: Morgan
##ID: 2
##Department: IVC
##
##Name: Loke
##ID: 10
##Department: IVC
##>>> 
