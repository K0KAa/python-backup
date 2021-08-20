import sys

try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("text cant be number")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(1)
print(f"x/y ={result}")