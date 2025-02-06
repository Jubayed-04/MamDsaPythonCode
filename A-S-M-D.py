# Python code to Add/subtract/multiply/divide 2 numbers

add = lambda  a, b: print(f"The addition is: {int(a+b)}")
sub = lambda  a, b: print(f"The subtraction is: {int(a-b)}")
multiplication = lambda a, b: print(f"The multiplication is: {int(a*b)}")
division = lambda a,b: print("Can not be divided by zero") if b == 0 else print(f"The division is {int(a/b)}")

print("Which operation will you want to perform?")
print("1/Addition, 2/Subtraction, 3/Multiplication, 4/Division")
choice = input(": ").lower()

if choice == "1" or choice == "addition":
    x = float(input("Enter a number: "))
    y = float(input("Enter another number to add: "))
    add(x, y)
elif choice == "2" or choice == "subtraction":
    x = float(input("Enter a number: "))
    y = float(input("Enter another number to subtract: "))
    sub(x, y)
elif choice == "3" or choice == "multiplication":
    x = float(input("Enter a number: "))
    y = float(input("Enter another number to multiply: "))
    multiplication(x, y)
elif choice == "4" or choice == "division":
    x = float(input("Enter a divisor: "))
    y = float(input("Enter a dividend: "))
    division(x, y)
else:
    print("Your input is invalid!")
