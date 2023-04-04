#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 12
my_rectangle.height = 5
print(my_rectangle.__dict__)


my_rectangle.width = "isaac"
my_rectangle.height = "lol"
print(my_rectangle.__dict__)
