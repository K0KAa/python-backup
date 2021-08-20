import functions
#from functions import square

num = int(input("Enter a number:"))

for i in range(num):
    print(f"the square of {i} is {functions.square(i)}")
