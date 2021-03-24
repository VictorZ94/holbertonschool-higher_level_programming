# Hello world in python 3

## Zen of python

The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language

```Bash
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Quiz questions

### Question #0

    - Who created Python?
    Guido van Rossum

### Question #1
    - What does this command line print?
    `>>> print("Holberton school")`
    Holberton school

### Question #2
    - What does this command line print?
    `>>> print("{:d} Battery street".format(98))`
    98 Battery street

### Question #3
    - What does this command line print?
   `>>> print("{:d} Battery street, {}".format(98, "San Francisco"))`
   98 Battery street, San Francisco

### Question #4
    - What does this command line print?
    `>>> a = "Python is cool"
    >>> print(a[4])`
    o

### Question #5
    - What does this command line print?
    `>>> a = "Python is cool"
    >>> print(a[0:6])`
    Python

### Question #6
    - What does this command line print?
    `>>> a = "Python is cool"
    >>> print(a[7:])`
    Python

### Question #7
    - What does this command line print?
    `>>> a = "Python is cool"
    >>> print(a[0:6])`
    is cool
### Question #8
    - What does this command line print?
    `>>> a = "Python is cool"
    >>> print(a[7:-5])`
    is

### Question #9
    - What does this command line print?
    `>>> a = "Python is cool"
    >>> print(a[-2])`
    o

## Task section

### 0. Run Python file

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

```Bash
victorz@VictorZ:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

victorz@VictorZ:~/py/0x00$ export PYFILE=main.py
victorz@VictorZ:~/py/0x00$ ./0-run
Holberton School
victorz@VictorZ:~/py/0x00$ 
```

### 1. Run inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
```Bash
victorz@VictorZ:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
victorz@VictorZ:~/py/0x00$ ./1-run_inline 
Holberton School: 98
victorz@VictorZ:~/py/0x00$ 

```

### 2. Hello, print

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

    - Use the function print

```Bash
victorz@VictorZ:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
victorz@VictorZ:~/py/0x00$

```

### 3. Print integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

    - You can find the source code here
|   - The output of the script should be:
        - the number, followed by Battery street,
        - followed by a new line
    - You are not allowed to cast the variable number into a string
    - Your code must be 3 lines long
    - You have to use the new print numbers tips (with .format(...))


```Bash
victorz@VictorZ:~/py/0x00$ ./3-print_number.py
98 Battery street
victorz@VictorZ:~/py/0x00$ 
```

### 4. Print float

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

    - You can find the source code here
    - The output of the program should be:
        - Float:, followed by the float with only 2 digits
        - followed by a new line
    - You are not allowed to cast number to string
    - You have to use the new print formatting tips (with .format(...))

```Bash
victorz@VictorZ:~/py/0x00$ ./4-print_float.py
Float: 3.14
victorz@VictorZ:~/py/0x00$ 
```
