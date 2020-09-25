# Python - Test-driven development

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

## Quiz Question

### Question #0

Is this a standardized way to comment a function in Python?
```python
/* Addition function */
def add(a, b):
    return a + b

```

    - NO

### Question #1

Is this a standardized way to comment a function in Python?
```python
"""" Addition function """
def add(a, b):
    return a + b
```

    - NO

### Question #2

Is this a standardized way to comment a function in Python?
```python
##########
# Addition function
##########
def add(a, b):
    return a + b
```

    - NO

### Question #3

Is this a standardized way to comment a function in Python?

```python
def add(a, b):
    """ Addition function """
    return a + b
```

    - Yes

### Question #4

Is this module correctly commented?
```python
#!/usr/bin/python3
""" 
    My calculation module
"""
import sys
...

```
    - Yes 

### Question #5
Is this module correctly commented?

```python
#!/usr/bin/python3
import sys

""" 
    My calculation module
"""
...

```

    - NO

### Question #6
Based on this code, what should all the test cases be? (select multiple)

```python
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list

```
    - empty list
    - list with one element (any type)
    - list with 2 different element (same type)
    - list with twice the same element (same type)
    - list with more than 2 times the same element (same type)
    - list with multiple types (integer, string, etc…)
    - not a list argument (ex: passing a dictionary to the method)

## Task Section

### 0. Integers addition

Write a function that adds 2 integers.
    - Prototype: `def add_integer(a, b=98):`
    - a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    - a and b must be first casted to integers if they are float
    - Returns an integer: the addition of a and b
    - You are not allowed to import any module
