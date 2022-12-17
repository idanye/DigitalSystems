import os
import sys
sys.path.append(r"C:\Users\idany\Uni_IDC\Second_Year_'22\Semester_1\Digital Systems\nand2tetris\projects\07")

from parser import Parser


if __name__ == '__main__':
    parser = Parser(r"C:\Users\idany\Uni_IDC\Second_Year_'22\Semester_1\Digital Systems\nand2tetris\projects\07\StackArithmetic\SimpleAdd\SimpleAdd.vm")
    print(parser.get_current_line())
    print(parser.command_type())
