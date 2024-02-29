# Converting bytes to string using decode()
data = b'TestString'
print(data)
print(type(data))

output = data.decode()
print(output, type(output))





# Converting bytes to string using str()
print("=" * 20, end="\n\n")
data = b'TestString'
print(data, type(data))

print(str(data))    # print(data.__str__())
print(data.__str__())
print(data) # --> print(str(data))  --> print(data.__str__())


output = str(data)  
# Not Converting data
# Getting the string representation of data

output = str(data, 'UTF-8')  
# Coverting the bytes object to string object
print(output, type(output))




# Using the 'codecs' module
import codecs
print("=" * 20, end="\n\n")
data = b'TestString'
print(data, type(data))

output = codecs.decode(data)
print(output, type(output))






# 'encode()' and 'decode()'
str1 = 'Python'
print("\nstr1 -->", type(str1))

dataBytes = str1.encode(encoding='utf-8')
print("\ndataBytes -->", type(dataBytes))

str2 = dataBytes.decode()
print("\nstr2 -->", type(str2))

print("str1 == str2 -->", str1 == str2, "\n")
