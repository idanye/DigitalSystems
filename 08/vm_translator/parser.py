from command_type import COMMAND_TYPE
import os

COMMENT_SYMBOL = "//"
WS_SYMBOL = " "


class Parser:
    def __init__(self, input_file):
        """
        Opens input file and ready to parse it
        :param input_file:
        """
        with open(input_file, "r") as opened_file:
            self.__file_content = opened_file.read().split("\n")
        self.__file_name = input_file
        self.__current_line_number = -1
        self.advance()

    def has_more_lines(self):
        """
        Checks if there are more lines in the input
        :return: True if there are more lines, otherwise False.
        """
        total_number_of_lines = len(self.__file_content) - 1
        if self.__current_line_number < total_number_of_lines:
            return True
        return False

    def advance(self):
        """
        Reads the next instruction from the input and makes it the current instruction
        """
        if self.has_more_lines():
            current_line = self.get_current_line()
            if not current_line.startswith(COMMENT_SYMBOL) and not current_line == "":
                self.__current_line_number += 1
            current_line = self.get_current_line()
            while self.has_more_lines() and (current_line.startswith(COMMENT_SYMBOL) or current_line == ""):
                self.__current_line_number += 1
                current_line = self.get_current_line()

    def get_current_line(self):
        """
        Returns the current instruction, skips over whitespaces and comments, if necessary
        :return: the current instruction
        """
        instruction = self.__file_content[self.__current_line_number]

        if COMMENT_SYMBOL in instruction:
            return instruction.split(COMMENT_SYMBOL)[0].strip()
        return instruction.strip()

    def command_type(self):
        """
        Returns a constant representing the type of the current command.
        If the current command is an arithmetic-logical command, returns C_ARITHMETIC
        :return: C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION
        C_RETURN, C_CALL
        """
        command = self.get_current_line().split(WS_SYMBOL)[0].upper()
        return COMMAND_TYPE[command.lower()]

    def arg1(self):
        """
        Returns the first argument of the current command.
        In the case for C_ARITHMETIC, the command itself (add, sub, etc.)
        :return:
        """
        if self.command_type() == "C_ARITHMETIC":
            return self.get_current_line().lstrip()
        elif self.command_type() != "C_RETURN":
            return self.get_current_line().split(WS_SYMBOL)[1]

    def arg2(self):
        """
        Returns the second argument of the current command.
        Should be called only if the current command is C_PUSH, C_POP,
        C_FUNCTION or C_CALL
        :return:
        """
        if self.command_type() == "C_PUSH" or self.command_type() == "C_POP" or self.command_type() == "C_FUNCTION" or self.command_type() == "C_CALL":
            return int(self.get_current_line().split(WS_SYMBOL)[2])

    def get_compressed_file_name(self):
        return self.__file_name
