from parser import Parser
from code_translator import CodeTranslator
from symbol_table import SymbolTable

class Hack_Assembler:
    def __init__(self, file_name):
        # opens an input file and process it
        # Constructs a symbol table and adds the predefined symbols to it
        self.__parser = Parser(file_name)
        self.__symbol = SymbolTable()


    def first_pass(self):
        # reads the program lines and add all symbols to symbol table
        # focuses on labels
        pass

    def second_pass(self):
        # translates a symbol to the symbol table
        pass

    def __output_file(self):
        # writes the string to the output file
        pass
