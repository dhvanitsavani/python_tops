def printLine():
    print("*"*50)

printLine()
print("welcome to user defined functions demo in python")
printLine()

def add(a, b):
    print("addition = ", a+b)

add(5, 10)
printLine()

def sub(a, b):
    return a - b

ans = sub(10, 4)
print("subtraction = ", ans)
print("subtraction = ", sub(10, 4))
printLine()

