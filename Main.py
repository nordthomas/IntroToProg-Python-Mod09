# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# TNord,9.2.2022,Added import code
#                Added menu and menu choice logic
#                Added code for menu choices 1 & 2
# TNord,9.3.2022,Added code for menu choices 3 & 4
#                Added error handling logic
#                Added file creation logic
# TNord,9.4.2022,Added option to delete employee data
#                Added loop for entering new employees
#                Code cleanup and polish
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from FileProcessor import FileProcessor as FP
    from IOClasses import EmployeeIO as IO
else:
    raise Exception("This file was not created to be imported")

str_filename = "EmployeeData.txt"
obj_filehandle = None
lst_employeedata = []

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
FP.create_file(file=obj_filehandle, file_name=str_filename) # If there is no file on disk, create one
lst_employeedata = FP.read_data_from_file(file_name=str_filename) # Read file in to a list

# Show user a menu of options
try:
    while(True):
        IO.print_menu_items()

        # Get user's menu option choice
        strchoice = IO.input_menu_options()

        # Show user current data in the list of employee objects
        if strchoice.strip() == '1':
            IO.print_current_list_items(list_of_rows=lst_employeedata)
            continue  # return to the menu

        # Let user add data to the list of employee objects
        elif strchoice == '2':
            while True:
                obj_employee = IO.input_employee_data()
                lst_employeedata.append(obj_employee)
                str_yn = input("Would you like to enter another employee (y/n)? ")
                if str_yn.lower() == "y":
                    continue
                else:
                    break
            continue  # return to the menu

        # Remove an existing employee object
        elif strchoice == '3':
            IO.print_current_list_items_numbered(list_of_rows=lst_employeedata)
            intDelete = int(IO.input_task_to_remove())
            IO.remove_data_from_list(emp_to_del=intDelete, list_of_rows=lst_employeedata)
            continue  # return to the menu

        # Let user save current data to file
        elif strchoice == '4':
            FP.save_data_to_file(file_name=str_filename, list_of_objects=lst_employeedata)
            continue  # return to the menu

        # Let user exit program
        elif strchoice == '5':
            print("Goodbye!")
            break  # exit loop

        else:
            print("Please enter a valid choice.")
            continue

except Exception as e:
    print(e, e.__doc__, type(e), sep='\n')
# Main Body of Script  ---------------------------------------------------- #
