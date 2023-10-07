


# Addition
def addition(x, y):
    z = x + y
    print(f"the sum of {x} and {y} is {z}")

# Subtraction
def subtraction(x, y):
    z = x - y
    print(f" if you minus {y} from {x}, it will give you {z}")

# Division
def division(x, y):
    z = x / y
    print(f"{x} divided by {y} will give you {z}")

# Multiplication
def multiplication(x, y):
    z = x * y
    print(f"{x} times {y} gives you {z}")

# Square root
def square(x, y):
    z = x ** y
    print(f"{x} square {y} gives you {z}")


while True:
    print("""
    1. Add
    2. Subtract
    3. Divide
    4. Multiply
    6. Square 
    5. Exit""")

    print()

    answer = input("Pick desired option (1, 2, 3, 4 or 5): ")

    if answer == "1":
        print("You picked the option add, please enter two numbers then click Enter.")
        a = eval(input("First number: "))
        b = eval(input("Second number: "))
        addition(a, b)

    elif answer == "2":
        print("You picked the option subtract, please enter two numbers then click Enter.")
        a = eval(input("First number: "))
        b = eval(input("Second number: "))
        subtraction(a, b)

    elif answer == "3":
        print("You picked the option divide, please enter two numbers then click Enter.")
        a = eval(input("First number: "))
        b = eval(input("Second number: "))
        division(a, b)

    elif answer == "4":
        print("You picked the option multiply, please enter two numbers then click Enter.")
        a = eval(input("First number: "))
        b = eval(input("Second number: "))
        multiplication(a, b)

    elif answer == "5":
        print("You picked the option square, please enter two numbers then click Enter.")
        a = eval(input("First number: "))
        b = eval(input("Second number: "))
        multiplication(a, b)

    elif answer == "6":
        print("Exiting...")
        break

    else:
        print("Your option was not found")









