#CALCULATOR

def add(x, y):
  return x+y
def sub(x, y):
  return x-y
def mult(x, y):
  return x*y
def div(x, y):
  return x/y
choice=0
while True:
  if choice==5:
    break
  try:
    num1=float(input("\nEnter the first number: "))
    num2=float(input("Enter the second number: "))
  except:
    print("Invalid Input! Please enter a number.")
    continue
  while True:
    try:
      print("\n1.Addition\n2.Subtaction\n3.Multiplication\n4.Division\n5.Exit")
      choice=int(input("Enter your choice: "))
      if choice == 1:
        print(f"{num1} + {num2} = {add(num1,num2)}")  
      elif choice == 2:
        print(f"{num1} - {num2} = {sub(num1,num2)}")  
      elif choice == 3:
        print(f"{num1} * {num2} = {mult(num1,num2)}")  
      elif choice == 4:
        print(f"{num1} / {num2} = {div(num1,num2)}")
      elif choice == 5:
        break
      else:
        print("Invalid Choice. Please enter a number between 1-5. ")
        continue
      break
    except:
      print("Invalid Choice. Please choose a number between 1-5. ")
      continue
