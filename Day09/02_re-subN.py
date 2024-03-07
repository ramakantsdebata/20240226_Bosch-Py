# 'subn' - Does the same job as 'sub', with a little difference
#           It returns a tuple
#               > first element - Updated string
#               > second element - No. of substitutoins done

import re

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

result = re.subn(r"[A-Z]{2,}", "INDEX", string)
print(type(result), result, sep="\n")
print()

result = re.subn(r"[A-Z]{2,}", "INDEX", string, 2)
print(type(result), result, sep="\n")
print()
