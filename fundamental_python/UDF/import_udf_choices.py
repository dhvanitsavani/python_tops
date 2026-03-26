import udf_choices

print("1. oddEven")
print("2. maxOfTwo")
print("3. maxOfThree")
print("4. prime")
print("5. fibonacci")
print("6. exit")
print("*"*40)

while True:
    choice = int(input("enter choice : "))

    if choice == 1:
        a = int(input("Enter a number : "))
        udf_choices.oddEven(a)
    elif choice == 2:
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        udf_choices.maxOfTwo(a, b)
    elif choice == 3:
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        c = int(input("Enter a number : "))
        udf_choices.maxOfThree(a, b, c)
    elif choice == 4:
        a = int(input("Enter a number : "))
        udf_choices.isPrime(a)
    elif choice == 5:
        a = int(input("Enter a number : "))
        udf_choices.fibonacci(a)
    elif choice == 6:
        print("Thank you for using our services")
        break
    else:
        print("Invalid choice, try agian")

    print("*"*40)


    
