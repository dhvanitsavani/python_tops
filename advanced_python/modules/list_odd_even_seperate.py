import random

mainList = []
oddList = []
evenList = []

for i in range(10):
    mainList.append(random.randint(1, 1000))

for i in mainList:
    if i % 2 != 0:
        oddList.append(i)
    else:
        evenList.append(i)

print("main list : ", mainList)
print("odd list : ", oddList)
print("even list : ", evenList)
