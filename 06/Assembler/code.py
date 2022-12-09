from types_of_dest import TypesOfDest
from types_of_comp import TypesOfComp
from types_of_jump import TypesOfJump

class Code:
    @staticmethod
    def dest(dest_inst):
        return TypesOfDest[str(dest_inst).upper()].value

    @staticmethod
    def comp(comp_inst):
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
        return TypesOfJump[str(jump_inst).upper()].value

