"""
You and a few of your classmates are trying to earn some extra money in the
evenings. To do so, you are repainting the numbers on mailboxes for a small
fee.

Since there are exactly ten of you in the group, you decide each person will
just concentrate on one digit! For example, one person will paint all of the
`1`s, someone else will paint all of the `2`s, etc.

Because of splitting up the labor in this way, you also need to split up the
payments as well. You need to figure out how many times each digit had to be
painted.

Write a function that can compute the number of times each digit was painted
given a `start` number and an `end` number.

**Example:**

For `start` = 125, and `end` = 132

The letterboxes are

- 125 = `1`, `2`, `5`
- 126 = `1`, `2`, `6`
- 127 = `1`, `2`, `7`
- 128 = `1`, `2`, `8`
- 129 = `1`, `2`, `9`
- 130 = `1`, `3`, `0`
- 131 = `1`, `3`, `1`
- 132 = `1`, `3`, `2`

The digit frequencies are 1 x `0`, 9 x `1`, 6 x `2`, etc.

and so the method would return `[1,9,6,3,0,1,1,1,1,1]`
"""
def paint_letterboxes(start, finish):
    # Your code here

