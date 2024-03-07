# (?{extn}{expr}) - Extension notation; Variety extension can be specified

# (?:{expr}) - Non caputring group

import re

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result)
print(result.groups())

result = re.search(r".+(\b.+ex\b).+(?:\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result)
print(result.groups())


## Named groups
# (?P<{name}>{pattern})
# (?P=name) - This is a back-referebce ti a previously named group

result = re.search(r".+(?P<wordex>\b.+ex\b).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string)
print(result)
print(result.groups())
print(result.group("wordex"))


## Assertions
#       LookAhead
#           Positive --> "{trgpattern}(?={chkpattern})"
#           Negative --> "{trgpattern}(?!{chkpattern})"
#       LookBehind
#           Positive --> "(?<={chkpattern}){trgpattern}"
#           Negative --> "(?<!{chkpattern}){trgpattern}"
