# from types_of_instructions import TypesOfInstructions
import types_of_instructions

COMMENT_SYMBOL = "//"


class Parser:
    def __init__(self, assembly_file_path):
        with open(assembly_file_path, "r") as opened_file:
            self.__file_content = opened_file.read().split("\n")
        self.__current_line_number = -1
        self.advance()

    def has_more_lines(self):
        total_number_of_lines = len(self.__file_content)
        if self.__current_line_number < total_number_of_lines:
            return True
        return False

    def advance(self):
        self.__current_line_number += 1
        while self.get_current_line().startswith(COMMENT_SYMBOL) or self.get_current_line() == "":
            self.__current_line_number += 1

    def get_current_line(self):
        return self.__file_content[self.__current_line_number]

    def instruction_type(self):
        a_instruction_symbol = str(types_of_instructions.TypesOfInstructions.A_INSTRUCTION.value)
        l_instruction_symbol = str(types_of_instructions.TypesOfInstructions.L_INSTRUCTION.value)

        if self.get_current_line().startswith(a_instruction_symbol):
            return str(types_of_instructions.TypesOfInstructions.A_INSTRUCTION.name)
        elif self.get_current_line().startswith(l_instruction_symbol):
            return str(types_of_instructions.TypesOfInstructions.L_INSTRUCTION.name)
        else:
            return str(types_of_instructions.TypesOfInstructions.C_INSTRUCTION.name)

    def symbol(self):
        if self.instruction_type() == types_of_instructions.TypesOfInstructions.A_INSTRUCTION.name:
            return str(self.get_current_line())[1:]
        elif self.instruction_type() == types_of_instructions.TypesOfInstructions.L_INSTRUCTION.name:
            return str(self.get_current_line())[1:-1]

    def dest(self, instruction):
        if instruction.instruction_type() == types_of_instructions.TypesOfInstructions.C_INSTRUCTION.name:
            match instruction:
                case types_of_instructions.TypesofDest.null.name:
                    return types_of_instructions.TypesofDest.null.value
                case types_of_instructions.TypesofDest.M.value:
                    return types_of_instructions.TypesofDest.M.value
                case types_of_instructions.TypesofDest.D.value:
                    return types_of_instructions.TypesofDest.D.value
                case types_of_instructions.TypesofDest.DM.value:
                    return types_of_instructions.TypesofDest.DM.value
                case types_of_instructions.TypesofDest.A.value:
                    return types_of_instructions.TypesofDest.A.value
                case types_of_instructions.TypesofDest.AM.value:
                    return types_of_instructions.TypesofDest.AM.value
                case types_of_instructions.TypesofDest.AD.value:
                    return types_of_instructions.TypesofDest.AD.value
                case types_of_instructions.TypesofDest.ADM.value:
                    return types_of_instructions.TypesofDest.ADM.value
