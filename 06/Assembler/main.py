import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from parser import Parser
from code import Code


if __name__ == '__main__':
    bla = Parser(r"C:\Users\idany\Uni_IDC\Second_Year_'22\Semester_1\Digital Systems\nand2tetris\projects\06\max\Max.asm")
    while bla.has_more_lines():
        print(f"The current instruction is: {bla.get_current_line()}")
        print(f"The type of the instruction is: {bla.instruction_type()}")
        if bla.instruction_type() == "A_INSTRUCTION" or bla.instruction_type() == "L_INSTRUCTION":
            print(f"The symbol of the instruction is: {bla.symbol()}")
        if bla.instruction_type() == "C_INSTRUCTION":
            print(f"DEST: {bla.dest()}\t|"
                  f" COMP: {bla.comp()}\t|"
                  f" JMP: {bla.jump()}")
            print(f"DEST BINARY: {Code.dest(bla.dest())}\t| COMP BINARY: {Code.comp(bla.comp())}\t| JMP BINARY: {Code.jump(bla.jump())}")
        bla.advance()
        print()
