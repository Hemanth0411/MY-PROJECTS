import random
while True:
    print(f"1.Roll the Dice\n2.To Exit")
    user = int(input("What do you want to do? "))
    if user == 1:
        number = random.randint(1, 6)
        if number == 1:
            print(number)
            print("You've got a one! It's a new beginning!")
            print()
        elif number == 2:
            print(number)
            print("Two twos make four! It's time to explore!")
            print()
        elif number == 3:
            print(number)
            print("A lucky three! Good fortune is on your side.")
            print()
        elif number == 4:
            print(number)
            print("Four fours mean stability and balance. Stay grounded!")
            print()
        elif number == 5:
            print(number)
            print("Five fives represent adventure and change. Embrace the unknown!")
            print()
        elif number == 6:
            print(number)
            print("Six sixes are a sign of triumph and victory. You've got this!")
            print()
    else:
        break
