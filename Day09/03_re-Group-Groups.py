# When we need to find matches for several distinct patterns in a target string.
# Operations which return a re.match object, can make use of group/groups
# 'group' - Tuple of all the matches found
# 'groups(idx)' - Used to access each individual match using the 'idx'.
#                 'idx' starts from 1
#                 if 'idx' is set to '0' or is omitted, it returns the entire matched string

import re

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
print(type(result), result, sep="\n")
print("\n\nresult.group() ->", result.group())
print("\nresult.groups() ->", result.groups())
print("\nresult.group(0) ->", result.group(0))
print("\nresult.group(1) ->", result.group(1))
print("\nresult.group(2) ->", result.group(2))

print("\n================================")

## Start & End ######################################
print(result.start(1), result.start(2))
print(result.end(1), result.end(2))

print(string[result.start(1):result.end(1)])
print(string[result.start(2):result.end(2)])


## Span ############################################
print(result.span(1))
print(result.span(2))

print(string[result.span(1)[0]:result.span(1)[1]])
print(string[result.span(2)[0]:result.span(2)[1]])
