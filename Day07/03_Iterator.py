# x = [1, 2, 3, 4, 5]
# s = "Hello"

# for i in x:
#     print(i, end="-")
# print("\n")
# for i in s:
#     print(i, end="-")
# print("\n")

# print("="*20)
# it = iter(x)
# for _ in range(len(x)):
#     print(next(it), end="-")
# print("\n")

# #########################################

# def IsIterable(obj):
#     try:
#         iter(obj)
#         print("Iterable")
#         return True
#     except TypeError:
#         print("Not an Iterable")
#         return False
    
# IsIterable(25)
# IsIterable([1, 2, 3])
# IsIterable("String")

# #######################################
print("\n", "#"*20, "\n")

class FibGen:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self
    
    def __next__(self):
        if self.count < self.num:
            x = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return x
        else:
            raise StopIteration
        
myFib = FibGen(10)
myIter = iter(myFib) # myFib._iter__()

for x in myIter:
    print(x, end=" - ")
print("Done")

#########################################

class Student:
    def ID(self):
        return id(self)

class Section:
    def __init__(self):
        self.mStudents = list()

    def PopulateList(self):
        for _ in range(10):
            print("Adding student...")
            self.mStudents.append(Student())

    def StudentCount(self):
        return len(self.mStudents)
    
    def __iter__(self):
        return iter(self.mStudents)

s1 = Section()
print(s1.StudentCount())
s1.PopulateList()
print(s1.StudentCount())

print("\n\n")
# for x in s1.mStudents:
#     print(x.ID())
for student in s1:
    print(student.ID())

# iter(s1) # s1.__iter__() ->> iter(mStudents)
    
print(type(iter(s1)))

