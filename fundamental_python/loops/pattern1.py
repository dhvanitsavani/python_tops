#1:-
for i in range(1, 6):
    print("* " * i)

#2:-
for i in range(1, 6):
    print(" "*(5-i), " *"*i)

#3:-
for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(j), end="")
    print()

#4:-
for i in range(2000, 3201):
    if i % 5 == 0:
        if i % 7 != 0:
            print(i, end=" ")
    
    
