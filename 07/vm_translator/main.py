from parser import Parser
from code_writer import CodeWriter
import sys


def main(file_name):
    parser = Parser(file_name)
    output_file_name = file_name.replace(".vm", ".asm")
    code_writer = CodeWriter(output_file_name)

    while parser.has_more_lines():
        code_writer.write_lst_to_file([f"// {parser.get_current_line()}"])
        if parser.command_type() == "C_ARITHMETIC":
            command = parser.arg1()
            code_writer.write_arithmetic(command)
        elif parser.command_type() == "C_PUSH" or parser.command_type() == "C_POP":
            command = parser.command_type().split("_")[1].lower()
            memory_type = parser.arg1()
            index = parser.arg2()
            code_writer.write_push_pop(command, memory_type, index)
        parser.advance()

    code_writer.end_of_program()
    code_writer.close()


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
