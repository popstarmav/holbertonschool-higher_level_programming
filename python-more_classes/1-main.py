#!/usr/bin/python3
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(sorted(my_rectangle.__dict__.items()))
my_rectangle.width = 10
my_rectangle.height = 3
print(sorted(my_rectangle.__dict__.items()))
