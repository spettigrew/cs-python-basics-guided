"""
You have been asked to implement a line numbering feature in a text editor that
you are working on.

Write a function that takes a list of strings and returns a new list that
contains each line prepended by the correct number.

The numbering starts at 1 and the format should be `line_number: string`. Make
sure to put a colon and space in between the `line_number` and `string` value.

Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""
def number(lines):
    # Your code here

def number(lines):
    if( len( lines ) < 1 ): return[]
    return_array = []
    for count, line in enumerate(lines):
        new_line = "%s: %s"

    new_lines = []
    index = 1
    for line in lines:
        new_lines.append(f"(index")

