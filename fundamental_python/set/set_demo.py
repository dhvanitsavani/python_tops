s1 = {1, 2, 3, 4, 10}
s2 = set([1, 2, 3, 4, "tops"])

print(s1)
print(s2)

s1.add(5)
print(s1)

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

s1.remove(1)
#s1.remove(6) => will give error
s1.discard(2)
s1.discard(6) # => won't give error
print(s1)
