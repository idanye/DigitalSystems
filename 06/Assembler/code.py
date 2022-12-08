from types_of_dest import TypesOfDest

class Code:
    @staticmethod
    def dest(dest_inst):
        return TypesOfDest[str(dest_inst).upper()].value


