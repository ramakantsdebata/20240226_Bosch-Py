# flags --> re.I | re.M | re.S | re.X

import re

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

string2 = '''The string is a
multiline comment
for testing
the behaviour of the method.
The test results will
be based on
these characters here.'''


## IGNORECASE ####################
print("\n## IGNORECASE ####################")
result = re.findall(r"the", string)
print("Result ->", result)

result = re.findall(r"the", string, re.I)
print("Result ->", result)

## MULTILINE ################
print("\n## MULTILINE ################")
result = re.findall(r"^The", string2)
print("Result ->", result)
print()

result = re.findall(r"^The", string2, re.M)
print("Result ->", result)
print()

result = re.findall(r"^The", string2, re.M|re.I)
print("Result ->", result)
print()

## DOTALL ####################
print("\n## DOTALL ####################")
result = re.findall(r".+", string2) # '.+' --> all chars, except newline
print("len(result) -->", len(result))
print("Result -->", result)
print()

result = re.findall(r".+", string2, re.S) # '.+' & 're.S' --> all chars, including newline
print("len(result) -->", len(result))
print("Result -->", result)
print()


## VERBOSE ########################
print("## VERBOSE ########################")
result = re.search(r'''.+\s     #Beginning off the string
                   (.+ex)       #Search for 'index'
                   .+           #Middle of the string, to be ignored later
                   (\d\d\s.+).  #Date at the end''', string, re.X)
if result is not None:
    print("\nresult.groups() ->", result.groups())
else:
    print("Pattern match failed!!")

