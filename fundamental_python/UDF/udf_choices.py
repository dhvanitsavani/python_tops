def oddEven(a):
    if a % 2 == 0:
        print(a, " is even")
    else:
        print(a, " is odd")

def maxOfTwo(a, b):
    if a > b:
        print(a, " is max")
    else:
        print(b, " is max")

def maxOfThree(a, b, c):
    if a > b:
        if a > c:
            print(a, " is max")
        else:
            print(c, " is max")
    elif b > c:
        print(b, " is max")
    else:
        print(c, " is max")

def isPrime(a):
    if a % 2 != 0:
        for i in range(3, int(a/2)+1, 2):
            if a % i == 0:
                print(a, " is not a prime number")
                break
        else:
            print(a, " is a prime number")
    else:
        print(a, " is not a prime number")

def fibonacci(n):
    a, b = 0, 1
    print(a, end=" ")

    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()
