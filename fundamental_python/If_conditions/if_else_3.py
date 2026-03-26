a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

if a > b:
    if a > c:
        print("a is max")
    else:
        print("c is max")
elif b > c:
    print("b is max")
else:
    print("c is max")
