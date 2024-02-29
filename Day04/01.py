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