prefix = [
    "interface", 
    "put",
    "local",
    "global"
]

delimiters = [
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    ":",
    ";",
    "$",
    "/"
]

data_types = [
    "num",
    "bool",
    "str",
    "ip",
    "ip-prefix",
    "ip6",
    "ip6-prefix",
    "id",
    "time",
    "nil"
]

esc_sequences = [
    "\"",
    "\\",
    "\n",
    "\r",
    "\t",
    "\$",
    "\?",
    "\_",
    "\a",
    "\b",
    "\f",
    "\v",
    "\xx"
]

arithmetic_operators = [
    "+",
    "-",
    "*",
    "/",
    "%"
]

relational_operators = [
    "=",
    "<",
    ">",
    "<=",
    ">=".
    "!="
]

logical_operators = [
    "!",
    "&&",
    "and",
    "||",
    "or",
    "in"
]

bitwise_operators = [
    "~",
    "|",
    "^",
    "&",
    ">>",
    "<<"
]

concatenation_operators = [
    ".",
    ","
]

other_operators = [
    "[]",
    "()",
    "$",
    "~",
    "->"
]

comments = [
    "#"
]

c_prefix = "red"
c_delimiters = "yellow"
c_data_types = "red"
c_esc_sequence = "orange"
c_operators = "lightblue"
c_arithmetic_operators = "lightblue"
c_relational_operators = "lightblue"
c_logical_operators = "lightblue"
c_bitwise_operators = "lightblue"
c_concatenation_operators = "lightblue"
c_other_operators = "lightblue"
c_comments = "green"
c_variables = "green"


def set_highligts(scr_input):

    new_color = "black"

    for letter in scr_input:
        if letter in delimiters:
            new_color = c_delimiters
        if letter in data_types:
            new color = c_data_types
        if letter in esc_sequences:
            new color = c_esc_sequence
        if letter in arithmetic_operators or relational_operators or logical_operators or bitwise_operators or concatenation_operators or other_operators:
            new color = c_operators
    for words in scr_input:
        if words in prefix:
            new_color = c_prefix
        if words in c_variables:
            new_color - c_variables
    
    print(new_color)

    return new_color