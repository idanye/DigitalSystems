
class CodeWriter:
    def __init__(self, output_file):
        """
        Opens input file and ready to parse it
        :param output_file:
        """
        self.__file = open(output_file, "w")
        self.__current_line_number = -1
        self.advance()

    def write_arithmetic(self, command):
        pass

    def write_push_pop(self, command, segment, index):
        pass

    def close(self):
        self.__file.close()


