# ---------------------------------------------------------- #
# Title: FileProcessor
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# TNord,9.3.2022,Added create_file method
#                Updated read_data_from_file to return list of objects instead of list of lists
# TNord,9.4.2022,Added import of DataClasses module for read_data_from_file
#                Code clean-up and polish
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    import DataClasses as DC

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        create_file(file, file_name):
        save_data_to_file(file_name,list_of_objects):
        read_data_from_file(file_name): -> (a list of objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        TNord,9.3.2022,Added create_file method
    """

    @staticmethod
    def create_file(file, file_name):
        """  Create empty file on disk

        :param file: (object) file handle:
        :param file_name: (string) name of file on disk:
        :return: nothing
        """
        try:
            if file == None:
                file = open(file_name, "a")
                file.close()
        except Exception as e:
            print("There was an error creating file!")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = DC.Employee(data[0], data[1], data[2].strip())
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

class DatabaseProcessor:
    pass
    # TODO: Add code to process to and from a database
