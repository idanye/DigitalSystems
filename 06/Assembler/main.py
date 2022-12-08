import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from parser import Parser
from code_translator import CodeTranslator
from symbol_table import SymbolTable


if __name__ == '__main__':
    bla = Parser("/Users/ority/Desktop/Studies/Digital systems/nand2tetris/repo/DigitalSystems/06/max/Max.asm")
    while bla.has_more_lines():
        print(f"The current instruction is: {bla.get_current_line()}")
        print(f"The type of the instruction is: {bla.instruction_type()}")
        if bla.instruction_type() == "A_INSTRUCTION" or bla.instruction_type() == "L_INSTRUCTION":
            print(f"The symbol of the instruction is: {bla.symbol()}")
        if bla.instruction_type() == "C_INSTRUCTION":
            print(f"DEST: {bla.dest()}\t| COMP: {bla.comp()}\t| JMP: {bla.jump()}")
            print(f"DEST BINARY: {CodeTranslator.dest(bla.dest())}\t| COMP: <>\t| JMP: <>")
        bla.advance()
        print()

    table = SymbolTable()
    table.add_entry("R0", 0)
    print(table.is_contain("R0"))
    print(table.get_address("R0"))
    print(table.is_contain("R1"))
    print(table.get_address("R1"))
