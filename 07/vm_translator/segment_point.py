from enum import Enum


class SegmentPointer(Enum):
    constant = "SP"
    local = "LCL"
    argument = "ARG"
    this = "THIS"
    that = "THAT"
    static = 16
    pointer = 0  # TODO: Need to update
    temp = 0
