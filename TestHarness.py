# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# TNord,9.4.2022,Updated code as FP.read_data_from_file now returns objects
#                Added error handline to test code
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from FileProcessor import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
try:
    objP1 = Emp(1, "Bob", "Smith")
    objP2 = Emp(2, "Sue", "Jones")
    lstTable = [objP1, objP2]
    for row in lstTable:
        print(row.to_string(), type(row))
except Exception as e:
    print(e, e.__doc__, type(e), sep='\n')

# Test processing module
try:
    Fp.save_data_to_file("EmployeeData.txt", lstTable)
    lstFileData = Fp.read_data_from_file("EmployeeData.txt")
    lstTable.clear()
    for line in lstFileData:
        lstTable.append(line)
    for row in lstTable:
        print(row.to_string(), type(row))
except Exception as e:
    print(e, e.__doc__, type(e), sep='\n')

# Test IO classes
try:
    Eio.print_menu_items()
    Eio.print_current_list_items(lstTable)
    print(Eio.input_employee_data())
    print(Eio.input_menu_options())
except Exception as e:
    print(e, e.__doc__, type(e), sep='\n')

