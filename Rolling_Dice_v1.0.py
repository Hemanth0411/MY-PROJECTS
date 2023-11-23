import random
while True:
    print(f"1.Roll the Dice\n2.To Exit")
    user=int(input("What do you want to do? "))
    if user==1:
        number=random.randint(1,6)
        print(number)
    else:
        break