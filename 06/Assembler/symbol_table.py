
PRE_DICT = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}
STARTING_INDEX = 16


class SymbolTable:
    def __init__(self):
        """
        Creates a new empty symbol table
        """
        self.__symbol_table = dict()
        self.__index = STARTING_INDEX

    def add_entry(self, symbol, address=None):
        """
        Adds new symbol to the table with its address.
        :param symbol: the symbol
        :param address: the address
        """
        if address is None:
            address = self.__index
            self.__index += 1
        self.__symbol_table.update({symbol: address})

    def is_contain(self, symbol):
        """
        Checks if the symbol table contains the given symbol
        :param symbol: the symbol
        :return: True if the table contains the symbol, otherwise False.
        """
        if symbol in self.__symbol_table:
            return True
        return False

    def get_address(self, symbol):
        """
        Returns the address associated with the symbol.
        :param symbol: the given symbol
        :return: the address that is associated with the given symbol.
        """
        if self.is_contain(symbol):
            return self.__symbol_table.get(symbol)

    def load_predefined_symbol(self):
        """
        Loads all the predefined symbols
        """
        for key in PRE_DICT.keys():
            self.add_entry(key, PRE_DICT[key])

