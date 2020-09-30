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
    if len(lines) < 1: return[]
    return_array = []
    for count, line in enumerate(lines):
        new_line = "%s: %s" % (count + 1, line)  # f"{count + 1}: {line}"
        return_array.append(new_line)
    return return_array

def number_2(lines):
    # Your code here
    # list I will return
    returned_list = []
    # iteration
    i = 0
    # looping to push each val in list
    for line in lines:
        i += 1
        returned_list.append(f"{i}: {line}")
    # return or print answer
    print(returned_list)

def number_3(lines):
    # Your code here
    new_lines = []
    index = 1
    for line in lines:
        new_lines.append(f"{index} : {line}")
        index += 1
    return new_lines
    
def number_insert(lines):
    new_lines = []
    for count, line in enumerate(lines):
        new_lines.insert(count, f"{count + 1}: line")

    return new_lines