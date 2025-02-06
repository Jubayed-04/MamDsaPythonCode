# Python code to delete a number from a stack data structure

stack = [0, 1, 5, 2]
print(f"stack: {stack}")
top = len(stack)

if top == 0:
    print("Underflow!")
    print("Can't remove any element!")
else:
    print("Do you want to delete a number? (yes/no)")
    choice = input(":").lower()
    if choice == "yes":
        stack.pop()
        print(f"stack: {stack}")
    else:
        pass

print(f"Top: {stack[len(stack)-1]}")
# will show the TOP data of the stack if that exists
