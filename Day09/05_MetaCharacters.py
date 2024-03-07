import re

string = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998. The panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."

# . - represents all chars, except newline
# A-Z, a-z, 0-9, $#  ?, : 

print("\n## . #######################")
result = re.search(r"(.+)", string)  # Just validating that the target has no newlines
print(result)
print(result.group(1))

if string == result.group(1):
    print("\nThere are indeed no newlines.")
else:
    print("\nThe target string has newline(s) in it.")


# ^ - Matches only at the beginning of the line
print("\n## ^ #######################")
result = re.search("^\w{3}", string)
print(result)
print()

stringT1 = "The Euro STOXX 600 index, which tracks all stock markets \
across Europe including the FTSE, fell by 11.48% – the worst day \
since it launched in 1998.\nThe panic selling prompted by the \
coronavirus has wiped £2.7tn off the value of STOXX 600 shares \
since its all-time peak on 19 February."
result = re.findall("^\w{3}", stringT1)
print(result)
print()

result = re.findall("^\w{3}", stringT1, re.M)
print(result)
print()


# $ - Matches at the end of the line
print("\n## $ ######################################")

result = re.findall(r"\s(\w{2,})\W$", stringT1)
print(result)
print()

result = re.findall(r"\s(\w{2,})\W$", stringT1, re.M)
print(result)
print()


# * - Matches 0 or more times, with as many repitions of
#     the preceeding expression as possible (in a GREEDY manner)
print("\n## * ################################")
result = re.findall(r"\d\d\d*", string)
print(result, "\n")

result = re.findall(r"E.*", string)
print(result, "\n")

result = re.findall(r"E\w*", string)
print(result, "\n")


# + - Matches 1 or more times, with as many repitions of
#     the preceeding expression as possible (in a GREEDY manner)
print("\n## + ################################")
result = re.findall(r"\d\d\d+", string)
print(result, "\n")

result = re.findall(r"E.+", string)
print(result, "\n")

result = re.findall(r"E\w+", string)
print(result, "\n")


# ? - Matches 0 or 1 time only (in a NON-GREEDY manner)
print("\n## ? ################################")
result = re.findall(r"\d\d\d?", string)
print(result, "\n")

result = re.findall(r"E.?", string)
print(result, "\n")

result = re.findall(r"E\w?", string)
print(result, "\n")


# Greedy vs. Non-Greedy ####################
#   *?
#   +?
#   ??

print("\n# Greedy vs. Non-Greedy ####################")

# Modifying the * 
result = re.findall(r"\d\d\d*", string)
print(result, "\n")

result = re.findall(r"\d\d\d*?", string)
print(result, "\n")

# Modifying the + 
result = re.findall(r"\d\d\d+", string)
print(result, "\n")

result = re.findall(r"\d\d\d+?", string)
print(result, "\n")



result = re.findall(r"E.*", string)
print(result, "\n")

result = re.findall(r"E.*?", string)
print(result, "\n")


result = re.findall(r"E.+", string)
print(result, "\n")

result = re.findall(r"E.+?", string)
print(result, "\n")

# Modifying the ?
result = re.findall(r"\d\d\d?", string)
print(result, "\n")

result = re.findall(r"\d\d\d??", string)
print(result, "\n")


## \ - can have either of the two roles:
#       1. Special sequence - \A \b \B \d \D \s \S \w \W
#       2. Escape character - Escaping and matchnig a symbol
#                             which otherwise has a special meaning
#                             \. \? \[ \] \( \) \^ \$ \{ \}

print("\n# \ ##################################")

# Special Sequence
result = re.findall(r"\d", string)
print(result)

# Escape symbold with special meaining
result = re.findall(r"\.", string)
print(result)


## [] - A set of characters and character class
# Quantifiers (* + ?)
print("\n## [] #####################################")

result = re.findall(r"[aeiou]", string)
print(result, "\n")

# positions =  [m.span()  for m in re.finditer(r"[aeiou]", string, re.I)]
positions =  [m.start()  for m in re.finditer(r"[aeiou]", string, re.I)]
print(positions, "\n")

positions =  [m.span()  for m in re.finditer(r"st", string, re.I)]
print(positions, "\n")


## Character Classes
print("\n## Character Classes ##########################")
result = re.findall(r"[a-d]", string)
print(result, "\n")

result = re.findall(r"[S-W]", string)
print(result, "\n")

result = re.findall(r"[1-5]", string)
print(result, "\n")

result = re.findall(r"[a-f][c-w]", string)
print(result, "\n")

result = re.findall(r"[0-5][7-9]", string)
print(result, "\n")

result = re.findall(r"[0-9][a-z]", string)
print(result, "\n")


# NEGATION - Use a caret inside the [], at the beginning
result = re.findall(r"[^X]", string)
print(result, "\n")
print("Is X present in the string?", 'X' in string)
print("Is X present in the result?", 'X' in result)


# Special characters lose thier special meaining, if inside []
result = re.findall(r"(.+?)", string)
print(result, "\n")

result = re.findall(r"[(.+?)]", string)
print(result, "\n")

# Whitespace characters
# space ( )
# newline(\n)
# tab (\t)
# vertical tab (\v)
# form feed (\f)
# carriage return (\r)

result = re.findall(r"[ \n\t\v\f\r]", string)
print("Count ->", len(result))
print(result, "\n")

# Opposite
result = re.findall(r"[^ \n\t\v\f\r]", string)
print("Count ->", len(result))
print(result, "\n")

# Alphanumeric
result = re.findall(r"[a-zA-Z0-9_]", string)
print("Count ->", len(result))
print(result, "\n")

# Opposite
result = re.findall(r"[^a-zA-Z0-9_]", string)
print("Count ->", len(result))
print(result, "\n")

## {} ###################################
result = re.findall(r"\b\w{4}\b", string)
print(result, "\n")

result = re.findall(r"\b\w{3,5}\b", string)
print(result, "\n")

result = re.findall(r"\b\w{3,}\b", string)
print(result, "\n")

number = "12345667697894634324554"
result = re.search(r"\d{3,6}", number)
print(result, "\n")

number = "12345667697894634324554"
result = re.search(r"\d{3,6}?", number)
print(result, "\n")


## | ################################################
# A|B|C - where A, B and C are distinct REs,
#         and the A|B|C matches either of A, B or C  

result = re.search(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string)
print(result, "\n")

result = re.search(r"\d{8}|\d{4}|\b[A-Z]{4}\b", string)
print(result, "\n")

