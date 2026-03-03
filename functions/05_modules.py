# there are two types of modules - 
# built-in modules -
import math
import os

print(math.sqrt(4)) # square root

# and external modules -
import mymodule
import requests

mymodule.hello()

r = requests.get("https://www.google.com")
print(r._content)