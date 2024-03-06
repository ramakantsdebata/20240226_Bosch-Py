__all__ = ['greet', 'greetName']

def greet():
    print("Hi there!!")

def greetName(name):
    strFinal = greetHelper(greeting="Hello", name=name)
    print(strFinal)

def greetHelper(greeting, name):
    return greeting + " " + name

def Test1():
    greetName("Ramakant")

def Test2():
    greet()

def Test3():
    print(greetHelper("Hi", "Rakesh"))

if __name__ == '__main__':
    Test1()
    Test2()
    Test3()
    
