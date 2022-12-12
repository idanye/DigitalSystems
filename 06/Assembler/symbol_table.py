
PRE_DICT = {
    "R0": 0,
    "R1": 1,
    "R0": 0,
    "R1": 1,
    "R0": 0,
    "R1": 1,
    "R0": 0,
    "R1": 1,
    "R0": 0,
    "R1": 1,
    "R0": 0,
    "R1": 1,
}

class SymbolTable:

    def __init__(self):
        self.__symbol_table = dict()

    def add_entry(self, symbol, address):
        self.__symbol_table.update({symbol: address})

    def is_contain(self, symbol):
        if self.__symbol_table.get(symbol) is not None:
            return True
        return False

    def get_address(self, symbol):
        if self.is_contain(symbol):
            return self.__symbol_table.get(symbol)

    def load_predefined_symbol(self):
