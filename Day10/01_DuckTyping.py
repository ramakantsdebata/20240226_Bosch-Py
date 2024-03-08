def Print(data):
    print(data)     # data --> str(data) --> data.__str__() --> data.__repr__()
    data += 1

class MyType:
    def __str__(self):
        return "This is an object of MyType."
    
    def __repr__(self):
        return f"Object {id(self)} not initialised."
    

def Test1():
    x = 10
    x = 10.1
    x = "Test"
    x = MyType()
    Print(x)

    a = 10
    b = MyType()
    print(add(a, b))

##########################################################
    
## Polymorphism

class Animal:
    def Speak(self):
        print("Not Implemented")

    def Eat(self):
        print("Munching...")

# class Dog(Animal):
class Dog:
    def Speak(self):
        print("Woof")

    def Eat(self):
        print("I can eat too.")

class Cat(Animal):
# class Cat:
    def Speak(self):
        print("Meow")

# class Cow(Animal):
class Cow:
    def Speak(self):
        print("Moo")

# def Talk2Animal(obj: Animal):
def Talk2Animal(obj):
    obj.Speak()

def Test2():
    Obj1 = Dog()
    Obj2 = Cat()
    Obj3 = Cow()

    Talk2Animal(Obj1)
    Talk2Animal(Obj2)
    Talk2Animal(Obj3)

    print("Is Cat an Animal?", isinstance(Obj2, Animal))
    print("Is Dog an Animal?", isinstance(Obj1, Animal))

    Obj2.Eat()
    Obj1.Eat()


if __name__ == "__main__":
    # Test1()
    Test2()