def add(x, y):
    return x + y


result = add(1, 2)
# python 3.5 dont accept the f string
#print(f"This is the sum: 1, 2, {result}")

print("This is the sum: 1, 2, %s" % result)
