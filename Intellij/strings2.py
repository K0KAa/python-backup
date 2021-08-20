parrot = "Norwegian Blue"

print(parrot)
print(parrot[4])

print()
print(parrot[-1])

print()

print(parrot[10:14])
print(parrot[10:])

print(parrot[:7] + parrot[7:])
print(parrot[:])

print()

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,445,556:343 545,667,870"
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
