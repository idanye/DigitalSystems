from segment_pointer import SegmentPointer
import os


class CodeWriter:
    def __init__(self, output_file):
        """
        Opens input file and ready to parse it
        :param output_file: string
        """
        self.__file_name = os.path.basename(output_file).split(".")[0]
        self.__file = open(output_file, "w")
        self.__label_index = 0

    def write_arithmetic(self, command):
        """
        Writes to the output file the assembly code that implements the given
        arithmetic-logical command.
        :param command: string
        """
        if command == "add":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("+", 2))
        if command == "sub":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("-", 2))
        if command == "neg":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("-", 1))
        if command == "not":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("!", 1))
        if command == "or":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("|", 2))
        if command == "and":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("&", 2))
        if command == "eq":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("JNE", 2, is_compare_operator=True))
            self.__label_index += 1
        if command == "gt":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("JLE", 2, is_compare_operator=True))
            self.__label_index += 1
        if command == "lt":
            self.write_lst_to_file(self.__translate_arithmetic_to_asm("JGE", 2, is_compare_operator=True))
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
        if command == "push":
            if segment == "constant":
                lst = self.__push_constant(segment, index)
            elif segment == "static":
                lst = self.__push_static(index, self.__file_name)
            else:
                lst = self.__push_regular_commands(segment, index)
        else:
            if segment == "static":
                lst = self.__pop_static(index, self.__file_name)
            elif segment != "constant":
                lst = self.__pop_regular_command(segment, index)

        self.write_lst_to_file(lst)

    def close(self):
        """
        Closes the output file
        """
        self.__file.close()

    def write_lst_to_file(self, array):
        """
        Adds the list to the file
        :param array: of the file lines
        """
        for line in array:
            self.__file.write("%s\n" % line)

    def end_of_program(self):
        """
        Adds an end program loop to the file
        """
        lst = ["// end of file", "(end)", "@end", "0;JMP"]
        self.write_lst_to_file(lst)

    def __translate_arithmetic_to_asm(self, sign, arg, is_compare_operator=False):
        """
        Translates an arithmetic command to an assembly command
        :param sign: the sign of the command
        :param arg: the arguments
        :param is_compare_operator: if it is =, <, >, =>, =<
        :return: the translation of the command as a list
        """
        temp = ""
        lst = ["@SP", "AM=M-1"]

        if is_compare_operator:
            temp = sign
            sign = "-"

        if arg == 2:
            lst.append("D=M")
            lst.append("@SP")
            lst.append("AM=M-1")
            lst.append(f"M=M{sign}D")

        elif arg == 1:
            lst.append(f"M={sign}M")

        if is_compare_operator:
            sign = temp
            lst.append(f"D=M")
            lst.append(f"@{sign}_{self.__label_index}")
            lst.append(f"D;{sign}")
            lst.append("@SP")
            lst.append("A=M")
            lst.append("M=-1")
            lst.append(f"@CONTINUE_{self.__label_index}")
            lst.append("0;JMP")
            lst.append(f"({sign}_{self.__label_index})")
            lst.append("@SP")
            lst.append("A=M")
            lst.append("M=0")
            lst.append(f"(CONTINUE_{self.__label_index})")

        lst.append("@SP")
        lst.append("M=M+1")
        return lst

    @staticmethod
    def __push_constant(segment, index):
        return [f"@{index}", "D=A", f"@{SegmentPointer[segment].value}", "A=M", "M=D", "@SP", "M=M+1"]

    @staticmethod
    def __push_static(index, file_name):
        return [f"@{file_name}.{SegmentPointer['static'].value + index}", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"]

    @staticmethod
    def __push_regular_commands(segment, index):
        lst = [f"@{index}", "D=A", f"@{SegmentPointer[segment].value}"]
        if segment == "temp" or segment == "pointer":
            lst.append("A=D+A")
        else:
            lst.append("A=M+D")
        lst.extend(["D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"])

        return lst

    @staticmethod
    def __pop_regular_command(segment, index):
        lst = [f"@{index}", "D=A", f"@{SegmentPointer[segment].value}"]
        if segment == "temp" or segment == "pointer":
            lst.append("D=D+A")
        else:
            lst.append("D=M+D")
        lst.extend(["@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"])

        return lst

    @staticmethod
    def __pop_static(index, file_name):
        return ["@SP", "AM=M-1", "D=M", f"@{file_name}.{SegmentPointer['static'].value + index}", "M=D" ]