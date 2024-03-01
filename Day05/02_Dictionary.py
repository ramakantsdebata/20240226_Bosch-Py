## Set = {key1, key2, key3, ...}
## Dict = {key1: value1, key2: value2, ...}
##          Keys    - Hashable / Immutable
##          VAlues  - Unrestricted
## Dict - Mutable


## states = ["Odisha", "Maharashtra", "Punjab"]
## capitals = ["Bhubaneswar", "Mumbai", "Chandigard"]

dt = {
    "Odisha": "Bhubaneswar", 
    "Maharashtra": "Mumbai", 
    "Punjab": "Chandigard"
    }

print(dt["Maharashtra"])

print("\n\n")
for state in dt.keys():
    print(state)

print("\n\n")
for capital in dt.values():
    print(capital)

print("\n\n")
print(len(dt))      # <-- Length ; No. of items/pairs in the dict
dt["WB"] = "Kolkata"

print("\n\n")
for state, capital in dt.items():
    print(state, "<<--->>", capital)

if "MP" in dt:
    print(dt["MP"])
else:
    print("Info not available")

print("Data ->", dt.get("MP"))

# dt["MP"]      --> KeyError Exception
# "MP" in dt    --> False, a bool value
# dt.get("MP")  --> None, if not present

# dt.update( <dict> )

x = dt.pop("Punjab")
print(x, ", ", dt)

x = dt.popitem()
print(x, ", ", dt)

dt.clear()