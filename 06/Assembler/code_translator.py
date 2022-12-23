from types_of_comp import TypesOfComp
from types_of_dest import TypesOfDest
from types_of_jump import TypesOfJump


class CodeTranslator:

    @staticmethod
    def dest(dest_inst):
        """
        :param dest_inst: gets the dest part of the C_INSTRUCTION
        :return: returns the binary code of the dest mnemonic
        """
        return TypesOfDest[str(dest_inst).upper()].value

    @staticmethod
    def comp(comp_inst):
        """
        :param comp_inst: gets the comp part of the C_INSTRUCTION
        :return: returns the binary code of the comp mnemonic
        """
        if comp_inst == "0":
            return TypesOfComp.zero.value
        if comp_inst == "1":
            return TypesOfComp.one.value
        if comp_inst == "-1":
            return TypesOfComp.minus_one.value
        if comp_inst == "D":
            return TypesOfComp.D.value
        if comp_inst == "A" or comp_inst == "M":
            return TypesOfComp.A.value
        if comp_inst == "!D":
            return TypesOfComp.not_D.value
        if comp_inst == "!A" or comp_inst == "!M":
            return TypesOfComp.not_A.value
        if comp_inst == "-D":
            return TypesOfComp.minus_D.value
        if comp_inst == "-A" or comp_inst == "-M":
            return TypesOfComp.minus_A.value
        if comp_inst == "D+1":
            return TypesOfComp.D_plus_one.value
        if comp_inst == "A+1" or comp_inst == "M+1":
            return TypesOfComp.A_plus_one.value
        if comp_inst == "D-1":
            return TypesOfComp.D_minus_one.value
        if comp_inst == "A-1" or comp_inst == "M-1":
            return TypesOfComp.A_minus_one.value
        if comp_inst == "D+A" or comp_inst == "D+M":
            return TypesOfComp.D_plus_A.value
        if comp_inst == "D-A" or comp_inst == "D-M":
            return TypesOfComp.D_minus_A.value
        if comp_inst == "A-D" or comp_inst == "M-D":
            return TypesOfComp.A_minus_D.value
        if comp_inst == "D&A" or comp_inst == "D&M":
            return TypesOfComp.D_and_A.value
        if comp_inst == "D|A" or comp_inst == "D|M":
            return TypesOfComp.D_or_A.value

    @staticmethod
    def jump(jump_inst):
        """
        :param jump_inst: gets the jump part of the C_INSTRUCTION
        :return: returns the binary code of the jump mnemonic
        """
        return TypesOfJump[str(jump_inst).upper()].value

    @staticmethod
    def get_binary_num(number):
        """
        Translate decimal number to binary
        :param number: decimal number
        :return: returns the number in binary representation
        """
        return '{0:016b}'.format(number)

    @staticmethod
    def get_c_instruction_binary(instruction):
        """
        Translate C_INSTRUCTION to binary
        :param instruction: parser object that contains the current line
        :return: the instruction in binary representation
        """
        dest = instruction.dest()
        bin_dest = CodeTranslator.dest(dest)
        comp = instruction.comp()
        bin_comp = CodeTranslator.comp(comp)
        jump = instruction.jump()
        bin_jump = CodeTranslator.jump(jump)
        if instruction.is_a_bit_on():
            a = "1"
        else:
            a = "0"
        return f"111{a}{bin_comp}{bin_dest}{bin_jump}"
