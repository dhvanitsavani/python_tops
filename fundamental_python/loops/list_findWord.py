list_1 = ["hello", "world", "learn", "python"]
target = "world"

for i in range(len(list_1)):
    if list_1[i] == target:
        print("found. index = ", i)
        break
else:
    print("not found")
