import random

num = random.randint(1, 20)

while True:
    guess = int(input("guess a number between 1 to 20 : "))

    if(guess == num):
        print("You guessed correct number.")
        break
    elif(guess > num):
        print("You guessed greater number.")
    else:
        print("You guessed smaller number.")
