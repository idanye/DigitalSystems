from command_type import COMMAND_TYPE


class CodeWriter:
    def __init__(self, output_file):
        """
        Opens input file and ready to parse it
        :param output_file: string
        """
        self.__file = open(output_file, "w")
        self.__label_index = 0

    def write_arithmetic(self, command):
        """
        Writes to the output file the assembly code that implements the given
        arithmetic-logical command.
        :param command: string
        """
        if command == "add":
            self.write_lst_to_file(self.__translate_arithm_to_asm("+", 2))
        if command == "sub":
            self.write_lst_to_file(self.__translate_arithm_to_asm("-", 2))
        if command == "neg":
            self.write_lst_to_file(self.__translate_arithm_to_asm("-", 1))
        if command == "not":
            self.write_lst_to_file(self.__translate_arithm_to_asm("!", 1))
        if command == "or":
            self.write_lst_to_file(self.__translate_arithm_to_asm("|", 2))
        if command == "and":
            self.write_lst_to_file(self.__translate_arithm_to_asm("&", 2))
        if command == "eq":
            self.write_lst_to_file(self.__translate_arithm_to_asm("EQ", 2, is_compare_operator=True))
            self.__label_index += 1
        if command == "gt":
            self.write_lst_to_file(self.__translate_arithm_to_asm("GT", 2, is_compare_operator=True))
            self.__label_index += 1
        if command == "lt":
            self.write_lst_to_file(self.__translate_arithm_to_asm("LT", 2, is_compare_operator=True))
            self.__label_index += 1

    def write_push_pop(self, command, segment, index):
        """
        Writes to the output file the assembly code that implements the given
        push or pop command
        :param command: (C_PUSH or C_POP)
        :param segment: string
        :param index: int
        """
        lst = []
        if not (command == "pop" and segment == "constant"):
            lst.append(f"@{index}")
            lst.append("D=A")
            lst.append("@SP")
            lst.append("A=M")
            lst.append("M=D")
            lst.append("@SP")
            lst.append("M=M+1")

        self.write_lst_to_file(lst)

    def close(self):
        """
        Closes the output file
        """
        self.__file.close()

    def __translate_arithm_to_asm(self, sign, arg, is_compare_operator=False):
        temp = ""
        lst = ["@SP", "AM=M-1"]

        if is_compare_operator:
            temp = sign
            sign = "-"

        if arg == 2:
            lst.append("D=M")
            lst.append("@SP")
            lst.append("AM=M-1")
            lst.append(f"M=D{sign}M")

        elif arg == 1:
            lst.append(f"M={sign}M")

        elif is_compare_operator:
            sign = temp
            lst.append(f"@TRUE{self.__label_index}")
            lst.append(f"D;J{sign}")
            lst.append("@SP")
            lst.append("A=M-1")
            lst.append("M=0")
            lst.append(f"@END_TRUE{self.__label_index}")
            lst.append("0;JMP")
            lst.append(f"(TRUE{self.__label_index})")
            lst.append("@SP")
            lst.append("A=M-1")
            lst.append("M=-1")
            lst.append(f"(END_TRUE{self.__label_index})")

        lst.append("@SP")
        lst.append("M=M+1")
        return lst

    def write_lst_to_file(self, array):
        for line in array:
            self.__file.write("%s\n" % line)
