x = ["manish", "abhijeet", "rakesh", "vinayak", "shankar"]

# MAP ###########################
# list(<seq>)
resMap = list(map(str.capitalize, x))
print("Mapped:", resMap)

# FILTER #######################
def HasR(word):
    if 'r' in str.lower(word):
        return True
    else:
        return False
    
resFil = list(filter(HasR, x))
print("Filtered:", resFil)

# REDUCE ########################

def Add(a, b):
    return a + " " + b

from functools import reduce
resRed = reduce(Add, x)
print("Reduced:", resRed)