#region Demo Open-Closed Principle
# Non-functional code
def add(x: int, y: int):
    return x + y

def sub(x: int, y: int):
    return x - y

class MyType:
    pass

def add(x: MyType, y: MyType):
    return x + y

#endregion

#region Using MultipleDispatch
from multipledispatch import dispatch

@dispatch(int, int)
def add(x: int, y: int):
    print("Add(int)")
    return x + y

@dispatch(float, float)
def add(x: float, y: float):
    print("Add(float)")
    return x + y

@dispatch(str, str)
def add(x: str, y: str):
    print("Add(str)")
    return x + y

add(1, 2)
add(1.1, 2.2)
add("One", "Two")
#endregion