x = 10
s1 = "Test"
lst = [1, 2, 3]

print(hash(x))
print(hash(s1))
# print(hash(lst)) <-- Unhasable

# Immutable can act as a key

# Set is a collection of key
# Set is Mutable
# Elements in a set have to be hashable/immutable

# set( <collection> ), OR {}

# Unordered 

st1 = {1, 2, 3}
st2 = {'a', 'b', 'c'}
st3 = {"Test", "String"}
# st4 = {st1, st2, st3}   <-- ERROR: Unhashable elements

# Lists can contain lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [l1, l2]

st1.add(4)
st1.add(3)
st1.update(l2)
st1.remove(4)
st1.discard(7)
print(st1)

print(st1.pop(), st1)
st4 = set(st1)
st1.clear()
print(st1)

st5 = {4, 5, 6, 7, 8, 9}
print(st4.union(st5))
# intersection  A & B
# difference    A - B
# Ex-or         A ^ B

st6 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(st4.issubset(st6))
print(st6.issuperset(st4))
print(st4.isdisjoint(st2))

# Sequence Unpacking
st7 = {1, 2, 3}
a, b, c = st7
print(a, b, c)


#####################################################
## FrozenSet - Immutable collection of unordered keys
fs1 = frozenset([1, 2, 3])
fs2 = frozenset(['a', 'b', 'c'])
fs3 = frozenset([fs1, fs2])

st8 = {fs1, fs2, fs3}
print(st8)
