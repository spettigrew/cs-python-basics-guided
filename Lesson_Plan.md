# CS Fundamentals in Python - Python Basics

## Training Kit

TODO: INSERT TRAINING KIT LINK
[]()

## Objectives

- install Python 3 on their local machine, run the interactive prompt in the terminal, and run Python files through the interpreter
- use a print statement
- use white space to denote blocks
- use basic types (integers, floats, strings) and interact with those types
- created formatted strings
- perform basic string operations
- evaluate conditional expressions and use boolean operators to control flow
- use for and while loops and break and continue statements
- use list comprehensions
- create user-defined functions and call them
- create user-defined classes and interact with instances of those classes
- perform basic dictionary operations
- import modules

---

## Before Class

### Instructor Resources

TODO: INSERT CORRECT LINKS HERE ONCE THEY ARE COMPLETE
- 🐙 [Guided Project Starter](https://github.com/LambdaSchool/Lesson-Plan-2.0/blob/master/www.example.com)
- 🐙 [Guided Project Solution](https://github.com/LambdaSchool/Lesson-Plan-2.0/blob/master/www.example.com)
- 🐙 [Training Kit GitHub Repo](https://github.com/LambdaSchool/Lesson-Plan-2.0/blob/master/www.example.com)

### Pre-class Announcement

Post the following in Slack at the start of Training Kit time.

```
Good morning! I hope you are excited to learn all about the basics of Python!

Remember, all of the "lecture" material is in Training Kit. During the Guided Project, we will be applying all of the skills and knowledge that you gain during your time going through the Training Kit this morning.

Here are the links you need for today:
* Training Kit - <insert link here>
* Guided Project Starter - <insert link here>
```

## During Class

### Start of Class Announcement

Post the following in Slack at the start of Guided Project time.

```
It's time to get started on our Guided Project!

Here are the objectives for today:
- install Python 3 on their local machine, run the interactive prompt in the terminal, and run Python files through the interpreter
- use a print statement
- use white space to denote blocks
- use basic types (integers, floats, strings) and interact with those types
- created formatted strings
- perform basic string operations
- evaluate conditional expressions and use boolean operators to control flow
- use for and while loops and break and continue statements
- use list comprehensions
- create user-defined functions and call them
- create user-defined classes and interact with instances of those classes
- perform basic dictionary operations
- import modules

Here are the links you need:
* Zoom - <insert link here>
* Slido - <insert link here>
* Guided Project Starter - <insert link here>
```

| Time Stamp | Activity                                  |
|------------|-------------------------------------------|
| 9:00       | Morning Announcement                      |
| 9:05       | Hook & Purpose                            |
| 9:10       | Demonstration 1: Breakouts                |
| 9:20       | Demonstration 2: Review with Entire Class |
| 9:30       | 5-Minute Break                            |
| 9:35       | Demonstration 2: Breakouts                |
| 9:45       | Demonstration 2: Review with Entire Class |
| 9:55       | 5-Minute Break                            |
| 10:00      | Slido Questions                           |
| 10:10      | Demonstration 3: Breakouts                |
| 10:20      | Demonstration 3: Review with Entire Class |
| 10:30      | 5-Minute Break                            |
| 10:35      | Demonstration 4: Breakouts                |
| 10:45      | Demonstration 4: Review with Entire Class |
| 10:55      | Conclusion & Preview                      |

### The Hook

Ask the following questions to the students and give them time to respond.

**How do you learn a new programming language? What are some of the strategies? What works best for you personally?**

After the students have had time to respond, you can share your own personal experience about learning new programming languages and what works best for you as an instructor.

### Purpose

Take some time to explain the following to the students.

**Why the students need to learn this material?**

Getting familiar with the basics of Python as quickly as possible is necessary because it is the language we will be using throughout the rest of our time together in Computer Science.

**What will they be able to do after learning this material?**

After achieving the objectives for today, you will be able to write basic Python programs.

**How will they show they have learned the material?**

You will show you have learned the material by completing all of the code challenges in Python in the module project.

### Learning Activities

The learning activities for this lesson are going to be solving a number of code challenges that will help  the students apply the basics of the Python language as well as get started with developing their problem-solving abilities as soon as possible.

If possible, these should be solved as small breakout groups where the students work together to solve the challenges and the instructor jumps around to the different break-out groups to provide support. Students can specifically ask for support by posting their breakout group number in the main slack channel.

---

### Demonstration 1

### Key Points

- appending to lists
- while loops
- slicing a string
- join() method on string class

### Guided Project

The following is adapted from this Kata: https://www.codewars.com/kata/5650ab06d11d675371000003/python

**Challenge Introduction:**

Define a function that transforms a given string into a new string where the original string was split into strings of a specified size.

For example:

```
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"
```

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.

**Starter Code:**

```python
def split_in_parts(s, part_length): 
    # your code here
    pass
```

**Solution Code:**

```python
def split_in_parts(s, part_length):
    str_parts = []
    i = 0
    while i < len(s):
        str_parts.append(s[i:i+part_length])
        i += part_length
        
    return " ".join(str_parts)
```

### Check for Understanding

Ask the students to post their solutions to the slack channel thread when everyone rejoins the main group. As an instructor review the solutions with the students, making sure to point out any errors to fix incorrect thinking or mental models that are apparent in the student's solutions.

---

### Demonstration 2

### Key Points

- string formatting
- the enumerate method
- list comprehensions

### Guided Project

The following is adapted from this Kata: https://www.codewars.com/kata/5650ab06d11d675371000003/python

**Challenge Introduction:**

You have been asked to implement a line numbering feature in a text editor that you are working on.

Write a function that takes a list of strings and returns a new list that contains each line prepended by the correct number.

The numbering starts at 1 and the format should be `line_number: string`. Make sure to put a colon and space in between the `line_number` and `string` value.

**Examples:**

```
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
```

**Starter Code:**

```python
def number(lines):
    #your code here
```

**Solution Code:**

```python
def number(lines):
    return ["%d: %s" % (idx, line) for idx, line in enumerate(lines, 1)]
```

### Check for Understanding

Ask the students to post their solutions to the slack channel thread when everyone rejoins the main group. As an instructor review the solutions with the students, making sure to point out any errors to fix incorrect thinking or mental models that are apparent in the student's solutions.

---

### Demonstration 3

### Key Points

- chained conditionals
- the enumerate method
- list comprehensions

### Guided Project

The following is adapted from this Kata: https://www.codewars.com/kata/57ef016a7b45ef647a00002d/train/python

**Challenge Introduction:**

Write a function that takes in a two-dimensional list (a list that contains lists) and returns a new list which contains only the lists from the original which:

1. were not empty
2. have items that are all of the same type

You can assume that the lists inside the list will only contain integers or strings. Also, for this challenge, we are assuming that empty arrays are not homogenous. Also, the resultant lists should be in the same order as the original list and none of the values should be changed.

**Example:**

Given `[[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]`, your function should return `[[1, 5, 4], ['b']]`.

**Starter Code:**

```python
def filter_homogenous(arrays):
    # your code
```

**Solution Code:**

```python
def filter_homogenous(arrays):
    homogenous = []
    
    for array in arrays:
        # filter out empty lists
        if len(array) == 0:
            continue
        # lists with 1 item are homogenous by definition
        elif len(array) == 1:
            homogenous.append(array)
        else:
            # check that all items in array of the same type
            if all(isinstance(item, type(array[0])) for item in array):
                homogenous.append(array)
                
    return homogenous
```

### Check for Understanding

Ask the students to post their solutions to the slack channel thread when everyone rejoins the main group. As an instructor review the solutions with the students, making sure to point out any errors to fix incorrect thinking or mental models that are apparent in the student's solutions.

---

### Demonstration 4

### Key Points

- chained conditionals
- the enumerate method
- list comprehensions

### Guided Project

The following is adapted from this Kata: https://www.codewars.com/kata/597d75744f4190857a00008d/train/python

**Challenge Introduction:**

You and a few of your classmates are trying to earn some extra money in the evenings. To do so, you are repainting the numbers on mailboxes for a small fee.

Since there are exactly ten of you in the group, you decide each person will just concentrate on one digit! For example, one person will paint all of the `1`s, someone else will paint all of the `2`s, etc.

Because of splitting up the labor in this way, you also need to split up the payments as well. You need to figure out how many times each digit had to be painted.

Write a function that can compute the number of times each digit was painted given a `start` number and an `end` number.

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

**Starter Code:**

```python
def paint_letterboxes(start, finish):
    # your code
```

**Solution Code:**

```python
def paint_letterboxes(start, finish):
    # initialize a list that starts the counts for each digit
    result = [0] * 10
    
    # the main loop that goes from starting number to finish number
    while start <= finish:
        current = start
        # increments the count for each digit in the current number
        while current != 0:
            # counts the rightmost digit
            result[current % 10] += 1
            # resets current with all the digits except the rightmost digit
            current = current // 10
        # increment outer loop
        start += 1
        
    return result
```

### Check for Understanding

Ask the students to post their solutions to the slack channel thread when everyone rejoins the main group. As an instructor review the solutions with the students, making sure to point out any errors to fix incorrect thinking or mental models that are apparent in the student's solutions.

---

## Conclusion & Preview

Take some time to reiterate the importance of diving into code challenges in order to quickly learn a new language and get comfortable with the fundamentals.

Talk about how that is what they will continue to do in the Module Project. They are attempting to continue building their problem-solving skills while quickly learning Python.

---

## After Class

### End of Class Announcement

### Module Project and Resources

```
Remember, in the module project, you are trying to quickly learn the fundamentals of Python while also building your problem-solving skills. You can reference the Training Kit materials in addition to the plethora of online resources (including the official docs) to help you solve the challenges in the module project.

Here is a link to the Module Project:
* Module Project Repo - <TODO: insert link here>
```

## Post Mortem

After class, take at least 5 minutes to reflect on the lesson you taught today. What would you change next time?

Change your lesson plan now, or jot down thoughts here, so you don't forget for the next cohort.
