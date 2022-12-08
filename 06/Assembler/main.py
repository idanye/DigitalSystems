from Assembler.parser import Parser


if __name__ == '__main__':
    bla = Parser(r"C:\Users\idany\Uni_IDC\Second_Year_'22\Semester_1\Digital "
                 r"Systems\nand2tetris\projects\06\add\Add.asm")
    # print(bla.has_more_lines())
    # print(bla.get_current_line())
    # print(bla.instruction_type())
    # bla.advance()
    # print(bla.get_current_line())
    # print(bla.instruction_type())
    print(bla.symbol())
    bla.advance()
    bla.advance()
    print(bla.symbol())
