from enum import Enum


class TypesOfInstructions(Enum):
    A_INSTRUCTION = "@"
    C_INSTRUCTION = None
    L_INSTRUCTION = "("


class TypesofDest(Enum):
    null = "000"
    M = "001"
    D = "010"
    DM = "011"
    A = "100"
    AM = "101"
    AD = "110"
    ADM = "111"
