# Tuple - Immutable ordered collection
# Elements - Unrestricted, Non-homogeneous
# Like Immutable Lists

# Zero-based, indexed, sliceable, nestable
# Can accept duplicates

# Creation
#   ctor - tuple()
#   ( <sequence> )
#   ( <objects> )

t1 = tuple(1, 2, 3)
t2 = ([1, 2, 3])
t3 = (1, 2, 3)


print(t3[1])
print(t1[1:])

t4 = (t1, t2, t3)