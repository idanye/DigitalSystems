from parser import Parser
from code_translator import CodeTranslator
from symbol_table import SymbolTable

class Hack_Assembler:
    def __init__(self, file_name):
        # opens an input file and process it
        # Constructs a symbol table and adds the predefined symbols to it
        self.__parser = Parser(file_name)
        self.__symbol = SymbolTable()
        self.__symbol.load_predefined_symbol()

    def first_pass(self):
        # reads the program lines and add all symbols to symbol table
        # focuses on labels
        while self.__parser.has_more_lines():
            if self.__parser.instruction_type() == "L_INSTRUCTION":
                self.__symbol.add_entry(self.__parser.symbol(), self.__parser.get_current_line_number())


    def second_pass(self):
        # translates a symbol to the symbol table
        pass

    def __output_file(self):
        # writes the string to the output file
        pass
