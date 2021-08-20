for i in range(1, 13):
    print("{0:2} has its cube of {1:4}".format(i, i**3))

print()
for i in range(1, 13):
    print("{0:2} has its cube of {1:^4}".format(i, i**3))

print()
print("Pi is app {0:12}".format(22/7))
print("Pi is app {0:12f}".format(22/7))
print(f"Pi is app {22/7:12.50f}")
print("Pi is app {0:52.50f}".format(22/7))
print("Pi is app {0:<62.50f}".format(22/7))
print("Pi is app {0:72.50f}".format(22/7))