# Search - Find the first occurance of the pattern
# SYNTAX - re.search(pattern, string, flags)

import re

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

result = re.search(r'\d{3}', string)
print(type(result), result)

print("Found ->", string[15:18])

if result is not None:
    print(result.span())
    print(result.start())
    print(result.end())
    print(string[result.start() : result.end()])