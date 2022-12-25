ARITHMETIC = "C_ARITHMETIC"

COMMAND_TYPE = {
    "push": "C_PUSH",
    "pop": "C_POP",
    "add": ARITHMETIC,
    "sub": ARITHMETIC,
    "neg": ARITHMETIC,
    "eq": ARITHMETIC,
    "gt": ARITHMETIC,
    "lt": ARITHMETIC,
    "and": ARITHMETIC,
    "or": ARITHMETIC,
    "not": ARITHMETIC,
    "label": "C_LABEL",
    "goto": "C_GOTO",
    "if-goto": "C_IF",
    "function": "C_FUNCTION",
    "call": "C_CALL",
    "return": "C_RETURN"
}
