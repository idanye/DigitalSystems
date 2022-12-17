from command_type import CommandType
from parser import Parser


class CodeWriter:
    def __init__(self, output_file):
        """
        Opens input file and ready to parse it
        :param output_file: string
        """
        self.__file = open(output_file, "w")

    def write_arithmetic(self, command):
        """
        Writes to the output file the assembly code that implements the given
        arithmetic-logical command.
        :param command: string
        """
        if command == str(CommandType.ADD.value).lower():
            self.__write_lst_to_file(self.__translate_arithm_to_asm("+", 2))
        if command == str(CommandType.SUB.value).lower():
            self.__write_lst_to_file(self.__translate_arithm_to_asm("-", 2))
        if command == str(CommandType.NEG.value).lower():
            self.__write_lst_to_file(self.__translate_arithm_to_asm("-", 1))
        if command == str(CommandType.OR.value).lower():
            self.__write_lst_to_file(self.__translate_arithm_to_asm("|", 2))
        if command == str(CommandType.EQ.value).lower():
            self.__write_lst_to_file(self.__translate_arithm_to_asm("=", 2))

    def write_push_pop(self, command, segment, index):
        """
        Writes to the output file the assembly code that implements the given
        push or pop command
        :param command: (C_PUSH or C_POP)
        :param segment: string
        :param index: int
        """
        pass

    def close(self):
        """
        Closes the output file
        """
        self.__file.close()

    @staticmethod
    def __translate_arithm_to_asm(sign, arg):
        lst = ["@SP", "M=M-1", "A=M", "D=M"]
        if arg == 2 and not sign == "=":
            lst.append("@SP")
            lst.append("M=M-1")
            lst.append("A=M")
            lst.append(f"M=D{sign}M")
        elif arg == 1:
            lst.append(f"M={sign}M")
        elif sign == "=":
            pass
        lst.append("@SP")
        lst.append("M=M+1")
        return lst

    def __write_lst_to_file(self, array):
        for line in array:
            self.__file.write("%s\n" % line)
