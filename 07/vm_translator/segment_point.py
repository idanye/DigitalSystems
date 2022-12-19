from enum import Enum


class SegmentPointer(Enum):
    constant = "SP"
    local = "LCL"
    argument = "ARG"
    this = "THIS"
    that = "THAT"
