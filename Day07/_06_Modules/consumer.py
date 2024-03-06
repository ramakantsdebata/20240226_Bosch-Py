# import greeter
# from greeter import greetName, greet
from greeter import *

greetName("Manish")
greet()

Test1() # <--Error: Not imported 

from greeter import Test1
Test1()