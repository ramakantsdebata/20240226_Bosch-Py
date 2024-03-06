# Compile - Compiles a regex pattern into a regex object,
#           which can be further used for matchin/searching

import re

s = r"\d\d\d\d"
s = r"\d{4}"

t = re.compile(s)
# print("t [" + str(t) + "] ->", type(t))

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

# print(string)

result = re.findall(t, string)
print(result)
print(dir(t))

result = re.findall(s, string)
print(result)


