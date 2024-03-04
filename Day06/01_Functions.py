# # Define Earlier (Python) vs. Define Higher

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

## ARGUMENT PASSING #####################################

## Positional Parameters
# def SumNums(n1, n2, n3):
#     sum  = n1 + n2 + n3
#     return sum

# def DiffNums(n1, n2, n3):
#     diff = n1 - n2 - n3
#     return diff

# print(SumNums(1, 2, 3))
# print(DiffNums(5, 3, 1))




## Default Arguments
# # def DiffNums(n1, n2):
# #     diff = n1 - n2
# #     return diff

# def DiffNums(n1, n2, n3 = 0):
#     diff = n1 - n2 - n3
#     return diff

# print(DiffNums(5, 3, 1))
# print(DiffNums(5, 3))




## Named Parameters / Keyword Arguments
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




# Packing Unpacking
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
def PrintData(a, *lst):   # *var <-- Packing the data into a collection
    print(a)
    if len(lst) < 1:      # Base case
        return 
    PrintData(*lst) # <-- Unpack the collection

l1 = [1, 2, 3, 4, 5]
PrintData(*l1)      # <-- Unpack the collection
# PrintData(a, *lst)
#       a -> 1:1 , Hence, first element is associated with 'a'
#       a = 1
#
#       *lst -> n:1, allows packing
#       lst = [2, 3, 4, 5]



## Variable-length Parameters
### Non-keyword arguments (*argv)
# def my_func(*args):
#     for arg in args:
#         print(arg, end='-')
#     print()

# my_func(1, 2, 3)
# my_func('a', 'b', 'c', 'd')
# l2 = "This is a string for testing.".split()
# my_func(*l2)



### Keyworded Arguments (**kwargs)
