n = int(input("Enter a number : "))

if n % 2 != 0:
    for i in range(3, int(n/2), 2):
        if n % i == 0:
            print(n, " is not a prime number", sep="")
            break
    else:
        print(n, " is a prime number", sep="")
else:
    print(n, " is not a prime number", sep="")
    
        
