from parser import Parser
from code_translator import CodeTranslator
from symbol_table import SymbolTable
import os
import sys


class HackAssembler:

    def __init__(self, file_name):
        """
        This function opens an input file and processes it.
        In addition, Constructs a symbol table and adds the predefined symbols to it.
        :param file_name: path to the file that the class is processing
        """
        self.__translated_code = []
        self.__file_name = file_name
        self.__parser = Parser(file_name)
        self.__symbol = SymbolTable()
        self.__symbol.load_predefined_symbol()

    def first_pass(self):
        """
        This function reads the program lines and adds all symbols to symbol table.
        It focuses on labels.
        """
        line_number = 0
        while self.__parser.has_more_lines():
            if self.__parser.instruction_type() == "L_INSTRUCTION":
                self.__symbol.add_entry(self.__parser.symbol(), line_number)
            if self.__parser.instruction_type() == "A_INSTRUCTION" or self.__parser.instruction_type() == "C_INSTRUCTION":
                line_number += 1
            self.__parser.advance()

    def second_pass(self):
        """
        translates the instructions into binary
        """
        self.__parser.go_to_start()
        while self.__parser.has_more_lines():
            if self.__parser.instruction_type() == "A_INSTRUCTION":
                symbol = self.__parser.symbol()
                if not symbol.isnumeric():
                    if not self.__symbol.is_contain(symbol):
                        self.__symbol.add_entry(symbol)
                    binary_num = CodeTranslator.get_binary_num(self.__symbol.get_address(symbol))
                else:
                    binary_num = CodeTranslator.get_binary_num(int(symbol))
                self.__translated_code.append(binary_num)
            if self.__parser.instruction_type() == "C_INSTRUCTION":
                binary_code = CodeTranslator.get_c_instruction_binary(self.__parser)
                self.__translated_code.append(binary_code)
            self.__parser.advance()

    def output_file(self):
        """
        This function creates a file that contains all the translated lines
        """
        output_file_name = os.path.basename(self.__file_name).split('.')[0] + ".hack"
        with open(output_file_name, 'w') as file:
            for line in self.__translated_code:
                file.write("%s\n" % line)


if __name__ == '__main__':
    path = sys.argv[1]
    assembler = HackAssembler(path)
    assembler.first_pass()
    assembler.second_pass()
    assembler.output_file()
