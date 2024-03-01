fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# newList = []
# for x in fruits:
#     if 'a' in x:
#         newList.append(x)


# Syntax - [ <output expr>      <iterate over existing coll>    <condition>/<Operation> ]
collection = [x     for x in fruits      if 'a' in x]
print("List ->", type(collection), collection)

collection = {x     for x in fruits      if 'a' in x}
print("Set ->", type(collection), collection)

collection = {x: x.capitalize()     for x in fruits      if 'a' in x}
print("Dictionary ->", type(collection), collection)

collection = (x     for x in fruits      if 'a' in x)
print("Generator ->", type(collection), collection)

collection = tuple(x     for x in fruits      if 'a' in x)
print("Tuple ->", type(collection), collection)
