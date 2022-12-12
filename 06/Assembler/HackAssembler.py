from parser import Parser
from code_translator import CodeTranslator
from symbol_table import SymbolTable

class Hack_Assembler:
    def __init__(self, file_name):
        # opens an input file and process it
        # Constructs a symbol table and adds the predefined symbols to it
        self.__translated_code = []
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
        self.__parser.go_to_start()
        while self.__parser.has_more_lines():
            if self.__parser.instruction_type() == "A_INSTRUCTION":
                symbol = self.__parser.symbol()
                if not self.__symbol.is_contain(symbol):
                    self.__symbol.add_entry(symbol, self.__parser.get_current_line_number())
                binary_num = CodeTranslator.get_binary_num(symbol)
                self.__translated_code.append(binary_num)
            if self.__parser.instruction_type() == "C_INSTRUCTION":
                binary_code = CodeTranslator.get_c_instruction_binary(self.__parser.get_current_line())
                self.__translated_code.append(binary_code)

    def __output_file(self):
        with open('prog.hack', 'w') as file:
            for line in self.__translated_code:
                file.write("%s\n" % line)