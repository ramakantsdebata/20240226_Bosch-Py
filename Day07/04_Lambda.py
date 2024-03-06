# Lambda - Annonymous function, Transient Functions, One-time use Func

def Square(num):
    return num ** 2

sq = lambda x : x**2
print(sq(3))

isEven = lambda x: x%2 == 0
print(isEven(11))

nextEven = lambda x: x+2 if x%2==0 else x+1
print(nextEven(11))

utilities = [lambda x : x**2, lambda x: x%2 == 0, lambda x: x+2 if x%2==0 else x+1]

print(utilities[2](12))