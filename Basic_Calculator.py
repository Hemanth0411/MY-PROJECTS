def add(x, y):
  return x+y
def sub(x, y):
  return x-y
def mult(x, y):
  return x*y
def div(x, y):
  return x/y

while True:
  print(f"1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
  choice=input("Enter your choice: ")
  if choice=='5':
    break
  while True:
    if choice in ('1','2','3','4'):
      num1=float(input("Enter the first number: "))
      num2=float(input("Enter the second number: "))

      if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
      elif choice =='2':
        print(num1, "-", num2, "=", sub(num1, num2))
      elif choice=='3':
        print(num1, "*", num2, "=", mult(num1, num2))
      elif choice =='4':
        print(num1, "/", num2, "=", div(num1, num2))
      break
    else:
      print(f"Invalid Input!\n")
      break



