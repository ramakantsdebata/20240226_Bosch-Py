from collections import namedtuple

Name = namedtuple('Name', ['First_Name', 'Last_Name'])
Student = namedtuple('Student', 'name age standard')
Student = namedtuple('Student', ['name', 'age', 'standard'])

s1 = Student("Ramakant", 14, 10)
print(s1[0], ", ", s1.name)
print(s1[1], ", ", s1.age)
print(s1[2], ", ", s1.standard)

print(hash(s1))


Point = namedtuple('Point', 'x y')
p1 = Point(10, 20)

print(p1.x, p1.y)


def MyHash(key):
    return key%10

empID = 1234
hash = MyHash(empID)
