# # Mutables
# lst1 = list()
# print(type(lst1), len(lst1), id(lst1))

# lst1.append(10)
# lst1.append("Test")
# lst1.append(10.5)
# print(type(lst1), len(lst1), id(lst1))
# print(lst1, "\n\n")


# lst2 = [1, 2, 3, "Manish", "Abhijeet"]
# print(lst2)
# print(lst2[3])

# print("Abhijeet" in lst2)

# lst2.insert(3, "String")
# print(lst2)

# lst3 = lst1 + lst2
# print(lst3)

# # "First""Second" --> Concatenation
# lst4 = ["Placeholder" * 5]
# print(lst4)

# lst5 = ["Placeholder"] * 5
# print(lst5)

# print(lst5.count('Placeholder'))

# lst2.reverse()
# print(lst2)

# lst6 = lst1.copy()


##############################################

# Effect of Mutability
## Immutables
str1 = "Rakesh"
str2 = str1
print(id(str1), id(str2))
str2 += "!!"
print(str1, str2)
print(id(str1), id(str2))

## Mutables
lst1 = [1, 2, 3, 4, 5]
# lst2 = lst1
lst2 = lst1[:]
lst3 = list(lst2)
lst2[1] = 200

print( lst1, "\n", lst2, "\n", lst3)
