import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from types_of_dest import TypesOfDest


class CodeTranslator:

    @staticmethod
    def dest(dest_inst):
        return TypesOfDest[str(dest_inst).upper()].value


