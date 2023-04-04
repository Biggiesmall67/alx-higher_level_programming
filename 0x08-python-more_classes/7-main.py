#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(10, 6)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(4, 3)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(9, 5)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["this", "is", "fun!"]
print(my_rectangle_3)

print("--")
