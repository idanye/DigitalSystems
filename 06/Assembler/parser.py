from types_of_instructions import TypesOfInstructions


COMMENT_SYMBOL = "//"
LEADING_SYMBOL_JUMP = ";"
LEADING_SYMBOL_COMP = "="


class Parser:
    def __init__(self, assembly_file_path):
        """
        Opens the input file/stream and gets ready to parse it
        :param assembly_file_path: input file
        """
        with open(assembly_file_path, "r") as opened_file:
            self.__file_content = opened_file.read().split("\n")
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

            while self.has_more_lines() and (current_line.startswith(COMMENT_SYMBOL) or current_line == ""):
                self.__current_line_number += 1
                current_line = self.get_current_line()

    def get_current_line(self):
        """
        Returns the current instruction, skips over whitespaces and comments, if necessary
        :return: the current instruction
        """
        instruction_without_ws = self.__file_content[self.__current_line_number].replace(" ", "")
        if COMMENT_SYMBOL in instruction_without_ws:
            return instruction_without_ws.split(COMMENT_SYMBOL)[0]
        return instruction_without_ws

    def instruction_type(self):
        """
        Returns the type of the current instruction
        :return: A_INSTRUCTION for @xxx, where xxx is either a decimal number or symbol.
                 C_INSTRUCTION for dest=comp;jump
                 L_INSTRUCTION for (xxx), where xxx is a symbol.
        """
        a_instruction_symbol = str(TypesOfInstructions.A_INSTRUCTION.value)
        l_instruction_symbol = str(TypesOfInstructions.L_INSTRUCTION.value)

        if self.get_current_line().startswith(a_instruction_symbol):
            return TypesOfInstructions.A_INSTRUCTION.name
        elif self.get_current_line().startswith(l_instruction_symbol):
            return TypesOfInstructions.L_INSTRUCTION.name
        else:
            return TypesOfInstructions.C_INSTRUCTION.name

    def symbol(self):
        """
        If the current instruction is (xxx) returns the symbol xxx.
        If the current instruction is @xxx, returns the symbol or decimal xxx.
        :return: the symbol
        """
        if self.instruction_type() == TypesOfInstructions.A_INSTRUCTION.name:
            return self.get_current_line()[1:]
        elif self.instruction_type() == TypesOfInstructions.L_INSTRUCTION.name:
            return self.get_current_line()[1:-1]

    def comp(self):
        """
        :return: Returns the symbolic comp part of the currect C_INSTRUCTION.
        """
        current_instruction = self.get_current_line()
        if self.instruction_type() == TypesOfInstructions.C_INSTRUCTION.name:
            if LEADING_SYMBOL_COMP in current_instruction:
                current_instruction = current_instruction.split(LEADING_SYMBOL_COMP)[1]

            if LEADING_SYMBOL_JUMP in current_instruction:
                current_instruction = current_instruction.split(LEADING_SYMBOL_JUMP)[0]

            return current_instruction

    def jump(self):
        """
        :return: Returns the symbolic jump part of the current C_INSTRUCTION.
        """
        current_instruction = self.get_current_line()
        if self.instruction_type() == TypesOfInstructions.C_INSTRUCTION.name:
            if LEADING_SYMBOL_JUMP in current_instruction:
                return current_instruction.split(LEADING_SYMBOL_JUMP)[1]

    def dest(self):
        """
        :return: Returns the symbolic dest part of the current C_INSTRUCTION.
        """
        current_instruction = self.get_current_line()
        if self.instruction_type() == TypesOfInstructions.C_INSTRUCTION.name:
            if LEADING_SYMBOL_COMP in current_instruction:
                return current_instruction.split(LEADING_SYMBOL_COMP)[0]

    def get_current_line_number(self):
        """
        :return: Returns the line number of the current instruction.
        """
        return self.__current_line_number

    def go_to_start(self):
        """
        This functions sets the index of the line numbers to point to the beginning of the file
        """
        self.__current_line_number = -1
        self.advance()

    def is_a_bit_on(self):
        """
        :return: True if the a-bit should be on, otherwise False.
        """
        if self.comp():
            if "M" in self.comp().upper():
                return True
        return False
