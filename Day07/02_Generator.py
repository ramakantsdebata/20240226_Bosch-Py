#region Basics
# def SimpleGeneratorFunc():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# for value in SimpleGeneratorFunc():
#     print(value, end="-")
# print()

# print("\n")

# it = SimpleGeneratorFunc()
# print(next(it), end = " - ")
# print(next(it), end = " - ")
# print(next(it), end = " - ")
# print(next(it), end = " - ")
# print(next(it), end = " - ")

#endregion

#region Fibonacci Generator
def FibGen(n):
    '''Generates a sequence of 'n' fibanacci numbers'''
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

# print(FibGen.__doc__)
    
it = FibGen(10)
print(type(it))

try:
    while(True):
        print(next(it), end=" - ")
except StopIteration:
    print("\nDone")

print("#"*25)
it1 = iter(FibGen(15))
try:
    while(True):
        print(next(it1), end=" - ")
except StopIteration:
    print("\nDone")


#endregion