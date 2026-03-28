oddSum = 0
evenSum = 0

dictionary = {
    "int1" : 15,
    "int2" : 18,
    "int3" : 201,
    "int4" : 100,
    "int5" : 105,
    "int6" : 9,
    "int7" : 333,
    "int8" : 154,
    "int9" : 10,
    "int10" : 18
}

for i in dictionary:
    if dictionary[i] % 2 == 0:
        evenSum = evenSum + dictionary[i]
    else:
        oddSum = oddSum + dictionary[i]

print("sum of odd = ", oddSum)
print("sum of even = ", evenSum)

