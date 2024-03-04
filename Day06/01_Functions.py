#region Define Earlier (Python) vs. Define Higher

# def Foo():
#     print("Foo")
#     Bar()

# def Bar():
#     print("Bar")
#     return 1

# def main():
#     print("Main")
#     Foo()

# main()

#endregion

## ARGUMENT PASSING #####################################

#region Positional Parameters
# def SumNums(n1, n2, n3):
#     sum  = n1 + n2 + n3
#     return sum

# def DiffNums(n1, n2, n3):
#     diff = n1 - n2 - n3
#     return diff

# print(SumNums(1, 2, 3))
# print(DiffNums(5, 3, 1))

#endregion

#region Default Arguments
# # def DiffNums(n1, n2):
# #     diff = n1 - n2
# #     return diff

# def DiffNums(n1, n2, n3 = 0):
#     diff = n1 - n2 - n3
#     return diff

# print(DiffNums(5, 3, 1))
# print(DiffNums(5, 3))

#endregion

#region Named Parameters / Keyword Arguments
# def DiffNums(n1, n2 = 0, n3 = 0):
#     diff = n1 - n2 - n3
#     return diff

# print(DiffNums(n1 = 5, n2 = 3, n3 = 1))
# print(DiffNums(n2 = 3, n1 = 5, n3 = 1))
# print(DiffNums(n1 = 5, n2 = 3))
# print(DiffNums(n1 = 5, n3 = 3))

# # Any argument with default value should have all args to it's right
# # also having default values
# def fileOpen(Name, Mode = 'r', encoding = 'utf-8'):
#     pass

# # fileOpen("Test.txt", Mode = "w", encoding = "utf-16")
# # fileOpen("Test.txt", encoding = "utf-16", Mode = "w")
# # fileOpen("Test.txt", encoding = "utf-16")
# # fileOpen("Test.txt", Mode = "w")
# # fileOpen("Test.txt")

#endregion

#region Packing Unpacking
# lst = list()        # New Object, with no elements
# # L-Value    R-Value
# # LHS        RHS
# # Location   Read

# # x = 10
# # y = x
# # 10 = x

# print(id(lst))


# lst = [x for x in range(3)]     # (1)Appending / (2)Overwriting / (3)New Object
# print(id(lst))
# x = "Test"
# x = "String"


# a, b, c = lst
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)

# print("=" * 10)
# lst1 = [x for x in range(5)]
# a, b, *c = lst1
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)

#####################################
## Iteration -1 
# def my_func(*args):
#     for arg in args:
#         print(arg, end=' ')
#     print()

# my_func(1, 2, 3)
# my_func('a', 'b', 'c', 'd')

## Iteration - 2
# By defualt, a packed collection is of type tuple. 
# We can explicitly specify it to beof a different type
# def PrintData(a, *lst):   # *var <-- Packing the data into a collection
#     print(a)
#     if len(lst) < 1:      # Base case
#         return 
#     PrintData(*lst) # <-- Unpack the collection

# l1 = [1, 2, 3, 4, 5]
# PrintData(*l1)      # <-- Unpack the collection
# PrintData(a, *lst)
#       a -> 1:1 , Hence, first element is associated with 'a'
#       a = 1
#
#       *lst -> n:1, allows packing
#       lst = [2, 3, 4, 5]
#endregion


## Variable-length Parameters
# region # Non-keyword arguments (*argv)
# def my_func(*args):
#     for arg in args:
#         print(arg, end='-')
#     print()

# my_func(1, 2, 3)
# my_func('a', 'b', 'c', 'd')
# l2 = "This is a string for testing.".split()
# my_func(*l2)

#endregion

#region # Keyworded Arguments (**kwargs)

# # Take-1
# def PrintWords(**kwargs):
#     for key, value in kwargs.items():
#         print("%s --> %s" % (key, value))

# PrintWords(first = "This", second = "is", third = "Python.")


# Take-2
# # RULE (A) - Keyworded args are always to the rightmost of the parameters passed

# def Func1(n1, n2, n3, n4, n5, n6, **nn):
#     print(type(nn))
#     for k, v in nn.items():
#         print("%s --> %d" % (k, v))
#     print("<<< %d >>>" % (nn['n8']))
#     print(f"<<< {nn['n8']} >>>")

# Func1(1, 2, 3, n4 = 4, n5 = 5, n6 = 6, n7 = 7, n8 = 8, n9 = 9)
# # Func1(1, 2, 3, n4 = 4, n5 = 5, n6 = 6, 7, 8, 9) # <-- Violates RULE (A)

#endregion

#region Special Arguments
## / : separates (positional-only) args from (positional or keyworded) args
## * : separates (positional or keyworded) args from (keyword-only) args 
# def fn1(a, b, c, /, d, e):
#     pass

# fn1(1, 2, 3, 4, 5)
# fn1(1, 2, 3, e = 5, d = 4)
# # fn1(1, 2, c = 3, e = 5, d = 4) # <-- Error: Pos-only as keyworded



# def fn2(a, b, c, /, d, e, *, f, g):
#     pass

# fn2(1, 2, 3, 4, e = 5, f = 6, g = 7)
# fn2(1, 2, 3, 4, 5, f = 6, g = 7)
# # fn2(1, 2, 3, 4, 5, 6, g = 7)    # <-- ERROR: Kworded-Only arg as Positional

#endregion


## SCOPES #################################

#region Variable Scope - 1
# L - Local scope
# E
# G - Global scope
# B

# s = "Global"

# def fn():
#     # global s
#     s = "Local"
#     print("Inside fn:", s)

# fn()
# print("Outside:", s)

#endregion

#region Variable Scope - 1
# L - Local scope
# E - Enclosing scope
# G - Global scope
# B

# s = "Global"

# def Outer():
#     s = "Local"
#     print("Inside Outer:", s)

#     def Inner():
#         s = "Inner"
#         # nonlocal s
#         print("Inside Inner:", s)
    
#     # print(type(Inner))
#     return Inner

# # fn = Outer()
# # fn()

# Outer()()
# print("Outside:", s)

#endregion


#region locals, globals
# L - Local scope
# E - Enclosing scope
# G - Global scope
# B - Built-in scope

# s = "Global"

# def Outer():
#     # print(type(globals()), globals())
#     # print("\n\n---------------------------")

#     s = "Local"
#     print("Inside Outer:", s)

#     print("Inside Outer (global s):", globals()['s'])

#     def Inner():
#         s = "Inner"
#         # nonlocal s
#         print("Inside Inner:", s)

#     print(type(locals()), locals())
#     print("\n\n---------------------------")


#     # print(type(Inner))
#     return Inner

# # fn = Outer()
# # fn()

# Outer()()
# print("Outside:", s)

#endregion