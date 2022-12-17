from parser import Parser


if __name__ == '__main__':
    parser = Parser("/Users/ority/Desktop/Studies/Digital systems/nand2tetris/repo/DigitalSystems/07/StackArithmetic/SimpleAdd/SimpleAdd.vm")
    print(parser.get_current_line())
    print(parser.command_type())
    print(f"first argument: {parser.arg1()}")
    print(f"second argument: {parser.arg2()}")

    parser.advance()
    parser.advance()
    print(parser.get_current_line())
    print(parser.command_type())
    print(f"first argument: {parser.arg1()}")
    print(f"second argument: {parser.arg2()}")

