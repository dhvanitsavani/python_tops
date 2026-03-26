import random

l = []
lucky = []

for i in range(1, 101):
    l.append(i)

for i in range(10):
    var = random.choice(l)
    
    lucky.append(var)
    l.remove(var)

print(lucky)
