import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = f"hello, {who_to_greet}"
    return greeting


print(greet('Dennis'))
print(greet("wanjeri"))

r = requests.get("https://www.google.com")
print(r)
