s1 = "Test"
len(s1)  # --> s1.__len__()

l1 = [1, 2, 3, 4, 5]
len(l1) # --> l1.__len__()

# strInterface = [attr       for attr in dir(str)    if attr.startswith('_') is False]
# print(strInterface)

strInterface = [attr for attr in dir(str) if callable(getattr(str, attr)) and attr.startswith('_') is False]
print(strInterface)
