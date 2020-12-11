def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def calculator():
  print("Select operation.")
  print("+.Add")
  print("-.Subtract")
  print("*.Multiply")
  print("/.Divide")

  while True:
    # Take input from the user
    choice = input("Enter choice(+,-,/,*): ")

    # Check if choice is one of the four options
    if choice in ('+', '-', '/', '*'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")