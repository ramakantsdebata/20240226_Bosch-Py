#region 1
# def add(a, b):
#     return a + b

# def add(a, b, c):
#     return a + b + c

# print(add(1, 2))
# print(add(1, 2, 3))
#endregion

#region 2
# def add(a, b, c = 0):
#     return a + b + c

# print(add(1, 2))
# print(add(1, 2, 3))
#endregion 

#region 3 
def add(dataType, *data):
    if(dataType == "str"):
        sum = ""
    else:
        sum = 0

    for x in data:
        sum = sum + x
    return sum

print(add("int", 1, 2))
print(add("int", 1, 2, 3))
print(add("float", 1.1, 2.2, 3.3))
print(add("str", "Test", "String"))
#endregion


## Why do we need Function Overloading?

#region 4
# def add(a: int, b: int):
#     sum = 0

#     sum = a + b
#     return sum

# def add(a: str, b:str):
#     res = a.concat(b)
#     return res

# print(add(1, 2))
# print(add("Test", "String"))
#endregion