import random

def rand(a, b, c, d):
    i = 0
    while i < d:
        yield random.choice(a) + " " + random.choice(b) + " " + random.choice(c)
        i += 1


for i in rand(["qwe", "rty", "uio", "asd"], ["123", "456", "789", "987"], ["fgh", "jkl", "zxc", "vbn"], 5):
    print(i)