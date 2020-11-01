"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""

# Font formatting

underline = '\u001b[4m'
default = '\u001b[0m'
bold = '\u001b[1m'
green = '\u001b[32m'
red = '\u001b[31m'


#


class Console:
    def __init__(self, student_service):
        self.__student_service = student_service

    def run_console(self):

        while True:
            self.print_menu()
            command_lst, args = self.get_user_input()
            command = command_lst[0]

            commands = ["add", "display", "filter", "undo", "exit"]

            try:
                if command not in commands:
                    raise Exception("The command you have typed does not belong to the list of commands.")

                if command == "add":
                    self.__student_service.add_student(args[0], int(args[1]))
                    print("You have successfully added a student.\n")
                elif command == "display":
                    self.print_all_students()
                elif command == "filter":
                    self.__student_service.filter_students(int(args[0]))
                    print("You have successfully filtered the list of students.\n")
                elif command == "undo":
                    self.__student_service.undo()
                    print("You have successfully undone the operation.\n")
                elif command == "exit":
                    return
            except Exception as ex:
                print("Error: ", ex)

    def print_all_students(self):
        li_students = self.__student_service.get_all_students()

        print(green + "The list of all students is: " + default)
        print(green + "Id, Name, Group" + default)
        for student in li_students:
            student.print_student()
        print("\n")

    @staticmethod
    def print_menu():
        print(underline + bold + "List of commands:" + default,
              "\n1.)" + green + " add \"Name\" \"Group\"" + default + " - Add a student",
              "\n2.)" + green + " display" + default + " - Display the list of students.",
              "\n3.)" + green + " filter \"Group\"" + default + " - Filter the list so that students in "
                                                                "a given group are deleted from the list.",
              "\n4.)" + green + " undo" + default + " - Undo the last operation that modified program data. "
                                                    "This step can be repeated.",
              "\n5.)" + red + " exit" + default)

    def get_user_input(self):
        command = input("What would you like to do?\n")
        li_command = self.format_input(command)
        args = li_command[1:]
        command = li_command[:1]
        return command, args

    @staticmethod
    def format_input(input_str):
        """
        Formats the input string into a list containing each word separately
        """
        li_command = input_str.split()

        if len(li_command) <= 2:
            return li_command

        for index1 in range(0, len(input_str)):
            if input_str[index1] == ' ':
                break

        for index2 in range(len(input_str) - 1, 0, -1):
            if input_str[index2] == ' ':
                break

        li_command = [input_str[:index1], input_str[index1+1:index2], input_str[index2:]]
        return li_command
