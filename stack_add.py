# Python code to add a number in a stack data structure

stack = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"The stack is: {stack}")

top = len(stack)
maxstk = 10
# maxstk  can be changed,

if top >= maxstk:
    print("Overflow!")
    print("Can't add any element!")
else:
    add = int(input("Enter an integer number to add: "))
    stack.append(add)
    print(f"Upgraded stack: {stack}")

# print(f"Top: {stack[len(stack)-1]}")
# will show the TOP data of the stack if that exists
