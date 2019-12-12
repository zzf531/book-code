def h1(name="yassob"):
    return 'h1' + name


print(h1())

greet = h1
print(greet())


del h1
# print(h1)  NameError: name 'h1' is not defined

print(greet())