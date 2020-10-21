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

