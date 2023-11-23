import random

print("Welcome to Dice Rolling Simulator!! ")
print()
print()
print("Do you want to roll the dice?")
x=input("Enter y for YES and n for NO:")
if x =="y":
    while x == "y":

# Generates a random number
# between 1 and 6 (including
# both 1 and 6)
        no = random.randint(1,6)

        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            print("One small step for you, one giant leap for luck!")
            print()
        if no == 2:
            print("[-----]")
            print("[  0  ]")
            print("[     ]")
            print("[  0  ]")
            print("[-----]")
            print("Two minds are better than one. Seek out a partner in your endeavors.")
            print()
        if no == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
            print("A steady three is a foundation for success. Build upon it wisely.")
            print()
        if no == 4:
            print("[-----]")
            print("[ 0 0 ]")
            print("[     ]")
            print("[ 0 0 ]")
            print("[-----]")
            print("Four corners represent stability and security. Find your anchor.")
            print()
        if no == 5:
            print("[-----]")
            print("[ 0 0 ]")
            print("[  0  ]")
            print("[ 0 0 ]")
            print("[-----]")
            print("Five senses are open to new experiences. Let your curiosity guide you.")
            print()
        if no == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
            print("Six sides of opportunity await. Embrace all that life has to offer.")
            print()

        x=input("press y to roll again and n to exit:")
        print("\n")
        if x=='n':
            exit
else:
    exit