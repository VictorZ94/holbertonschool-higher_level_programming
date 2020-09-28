# Python - More Classes and Objects

## Section task

### 0. Simple rectangle
Write an empty class Rectangle that defines a rectangle:

    - You are not allowed to import any module
```Bash
[victorz@ManjaroKDE 0x08-python-more_classes]$ cat 0-main.py 
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
[victorz@ManjaroKDE 0x08-python-more_classes]$ ./0-main.py 
<class '0-rectangle.Rectangle'>
{}
[victorz@ManjaroKDE 0x08-python-more_classes]$

```