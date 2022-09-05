# ---------------------------------------------------------- #
# Title: IOClasses
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# TNord,9.2.2022,Minor polish and clean-up
# TNord,9.3.2022,Tweaked print_current_list_items
# TNord,9.4.2022,Added input_task_to_remove method
#                Added remove_data_from_list method
#                Added print_current_items_list_numbered method
#                Added error handling
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else: 
    import DataClasses as DC

class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():
        input_menu_options(): -> (str)
        print_current_list_items(list_of_rows):
        print_current_list_items_numbered(list_of_rows):
        input_employee_data(): -> (object)
        input_task_to_remove(): -> (str)
        remove_data_from_list(task_to_del, list_of_rows): -> (list)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        TNord,9.2.2022,Minor polish and clean-up
        TNord,9.3.2022,Tweaked print_current_list_items
        TNord,9.4.2022,Added input_task_to_remove method
                       Added remove_data_from_list method
                       Added print_current_items_list_numbered method
                       Added error handling
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        try:
            print('''
            Menu of Options
            1) Show current employee data
            2) Add new employee data
            3) Remove employee data
            4) Save employee data to file
            5) Exit program
            ''')
            print()  # Add an extra line for looks
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        try:
            choice = str(input("Which option would you like to perform? [1 to 5]: ")).strip()
            print()  # Add an extra line for looks
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        try:
            print("******* The current employees are: *******")
            print("Employee ID | First Name | Last Name")
            for row in list_of_rows:
                print(str(row))
            print("*******************************************")
            print()  # Add an extra line for looks
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def print_current_list_items_numbered(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        try:
            print("******* The current employees are: *******")
            print("Employee ID | First Name | Last Name")
            i = 0  # Set a variable so we can label our row numbers
            for row in list_of_rows:
                i += 1  # Increment our row number
                print("(" + str(i) + ")" + " " + str(row))  # Print our table with row numbers for easier usability
                # print(str(row.employee_id)
                #       + ","
                #       + row.first_name
                #       + ","
                #       + row.last_name)
            print("*******************************************")
            print()  # Add an extra line for looks
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def input_employee_data():
        """ Gets data for an employee object

        :return: employee (object) with input data
        """
        try:
            eid = input("What is the employee ID? ").strip()
            fname = str(input("What is the employee First Name? ").strip())
            lname = str(input("What is the employee Last Name? ").strip())
            print()  # Add an extra line for looks
            emp = DC.Employee(eid, fname, lname)
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
        return emp

    @staticmethod
    def input_task_to_remove():
        """  Gets the row number to be removed from the list

        :return: (string)
        """
        try:
            remove = input("\nWhat row number would you like to delete? ").strip()
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
        return remove

    @staticmethod
    def remove_data_from_list(emp_to_del, list_of_rows):
        """ Removes data from a list of objects

        :param emp_to_del: (string) for row to delete:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of objects
        """
        try:
            if emp_to_del >= 1 and emp_to_del <= len(list_of_rows):
                del list_of_rows[emp_to_del - 1]  # Delete the indicated row
                if len(list_of_rows) == 0:
                    print("\nThere are no employees in the list.")
                else:
                    print(f"\nRow {emp_to_del} has been deleted.\n")  # Tell the user the row they selected has been deleted
                    print("******* The current employees are: *******")
                    print("Employee ID | First Name | Last Name")
                    for row in list_of_rows:  # Display the new list of employees
                        print(row)
                    print("*******************************************")
            else:
                print("Please enter a valid number.")
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows
