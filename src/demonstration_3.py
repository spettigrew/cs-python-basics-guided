"""
Write a function that takes in a two-dimensional list (a list that contains
lists) and returns a new list which contains only the lists from the original
which:

1. were not empty
2. have items that are all of the same type

You can assume that the lists inside the list will only contain integers or
strings. Also, for this challenge, we are assuming that empty arrays are not
homogenous. Also, the resultant lists should be in the same order as the
original list and none of the values should be changed.

**Example:**

Given `[[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]`, your function should
return `[[1, 5, 4], ['b']]`.
"""
from functools import reduce
def filter_homogenous(arrays):
    # Your code here
    newArray = []
    for array in arrays:
        print("array: ", array)
        if len(array) == 0:
            continue
        if len(array) == 1:
            newArray.append(array)
            continue
        is_homogenous = True
        for i in range(len(array) - 1):
            # while i < len(array) - 1:
            if type(array[i]) != type(array[i + 1]):
                is_homogenous = False
        if is_homogenous:
            newArray.append(array)
            print("Added array to newArray", newArray)
        print("is homogenous: ", is_homogenous)
        # i += 1
    print(newArray)

def filter_homogenous_reduce(arrays):
    return_array = []
    for list in arrays:
        if len(list) < 1: continue
        homogenous = reduce(type_check, list, list[0])
        if homogenous:
            return_array.append(list)
    return return_array

def type_check(x, y):
    if type(x) == type(y):
        return x
    return False


    print(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]))
    # def filter_homogenous(arrays):
    #     # iterate through the outer list
    #     new_list = []
    #     for outer_item in arrays:
    #         for inner_item in outer_item:
    #             # iterate through the inner list, check the values
    #             if (inner_item.isinstance(outer_item)):
    #                 new_list.append(inner_item)
    #     return new_list