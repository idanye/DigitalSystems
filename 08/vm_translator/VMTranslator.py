from parser import Parser
from code_writer import CodeWriter
import sys
import os


def is_file(path):
    if os.path.isfile(path):
        return True
    return False


def get_all_vm_files(given_folder_path):
    files_list = []
    for file in os.listdir(given_folder_path):
        if file.endswith(".vm"):
            files_list.append(os.path.join(given_folder_path, file))

    return files_list


def get_folder_name(path):
    return os.path.basename(path)


def main(path):
    parsers = []
    if is_file(path):
        parser = Parser(path)
        output_file_name = path.replace(".vm", ".asm")
        code_writer = CodeWriter(output_file_name)
        parsers.append(parser)
    else:
        for file_name in get_all_vm_files(path):
            parsers.append(Parser(file_name))
        folder_name = get_folder_name(path)
        output_file_name = folder_name.replace(".vm", ".asm")
        code_writer = CodeWriter(output_file_name)

    for parser in parsers:
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
            elif parser.command_type() == "C_LABEL":
                label = parser.arg1()
                code_writer.write_label(label)
            elif parser.command_type() == "C_FUNCTION":
                function_name = parser.arg1()
                args_number = parser.arg2()
                code_writer.write_function(function_name, args_number)
            elif parser.command_type() == "C_CALL":
                function_name = parser.arg1()
                args_number = parser.arg2()
                code_writer.write_call(function_name, args_number)
            elif parser.command_type() == "C_RETURN":
                code_writer.write_return()
            elif parser.command_type() == "C_GOTO":
                label = parser.arg1()
                code_writer.write_goto(label)
            elif parser.command_type() == "C_IF":
                label = parser.arg1()
                code_writer.write_if(label)

            parser.advance()

    code_writer.end_of_program()
    code_writer.close()


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
