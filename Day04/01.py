## Object
# Identity (funcion of address)
#       id(x)
# Type (of data it holds)
#       type(x), type(int)
# Value (it holds)
#       x

## Equality vs Equivalence

# x = 10
# print(id(x))

# y = 10
# print(id(y))
# y += 1
# y -= 1
# print(id(y))

# print(type(x))


###################################

x = 10
print(x, type(x), id(x))
x += 1
print(x, type(x), id(x))


print("#" * 20)
s1 = "Test"
print(id(s1))
s1 = "void"
print(id(s1))