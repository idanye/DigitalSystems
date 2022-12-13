from parser import Parser
from code_translator import CodeTranslator
from symbol_table import SymbolTable


class HackAssembler:
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
        line_number = 0
        while self.__parser.has_more_lines():
            if self.__parser.instruction_type() == "L_INSTRUCTION":
                self.__symbol.add_entry(self.__parser.symbol(), line_number)
            if self.__parser.instruction_type() == "A_INSTRUCTION" or self.__parser.instruction_type() == "C_INSTRUCTION":
                line_number += 1
            self.__parser.advance()

    def second_pass(self):
        # translates a symbol to the symbol table
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
        with open('prog.hack', 'w') as file:
            for line in self.__translated_code:
                file.write("%s\n" % line)

if __name__ == '__main__':
    assembler = HackAssembler(
        "/Users/ority/Desktop/Studies/Digital systems/nand2tetris/repo/DigitalSystems/06/rect/Rect.asm")
    assembler.first_pass()
    assembler.second_pass()
    assembler.output_file()
