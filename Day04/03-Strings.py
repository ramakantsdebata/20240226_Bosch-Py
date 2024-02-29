# Quotes
## Single Quotes
x = 'test'

## Double Quotes
x = "test"

s1 = "This is Abhijeet's notebook"
s2 = 'He said, "Thank you", upon returning it.'

## Triple quoting (Single/double quotes)
y = ''' This is
a multiline
string.'''
print(y)

helpText = """Usage:--------
Syntax: -------
Switches:
    a - asfadsfa
    b - asdfasd
    c - asdfasdf"""
print(helpText)

s2 = "First""Second"
print(s2)

## Reference - Escape sequences
##          https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences
## Reference - Format Specifiers
##          https://docs.python.org/3/library/string.html#format-specification-mini-language

program = 'Python'
days = 10

s1 = f"We are in a {program} training for {days} days."
fmt = "We are in a %s training for %d days." 
s2 = fmt%(program, days)

print(s1)
print(s2)


# Slicing
# [start : stop : step]
print(s1[5:15])
print(s1[5:])
print(s1[:15])
print(s1[::2])      # Even positions
print(s1[1::2])     # Odd positions
print(s1[::-1])