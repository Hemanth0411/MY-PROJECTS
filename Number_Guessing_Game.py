import random

print("Welcome to Number Guessing Game!")
print()
name=input("Enter your name:")
print("Hello, ",name)
print("Let the game Begin:")
true_number=random.randint(1,100)
guess_number=int(input("Enter your guess between 1 and 100: "))

while True:
    if guess_number==true_number:
        print("You are right! Good Job.")
        break
    elif guess_number>true_number:
        x=abs(guess_number-true_number)
        if x>10:
            print("Your guess is too high, Please try again.")
        else:
            print("Your guess is just a bit higher, try again.")
        guess_number=int(input("Enter your guess between 1 and 100: "))

    elif guess_number<true_number:
        x=abs(guess_number-true_number)
        if x>10:
            print("Your guess is too low, Please try again.")
        else:
            print("Your guess is just a little low, try again.")
        guess_number=int(input("Enter your guess between 1 and 100: "))
        