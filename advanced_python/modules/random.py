import random

# randint :-
n = random.randint(1, 100)
print(n)

# choice :-
l = []

for i in range(10):
    l.append(random.randint(1, 100))

print(l)
print(random.choice(l))
