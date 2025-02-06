# Python code to add a number in an array

array = [1, 2, 3, 4, 5, 5]
print(f"Array: {array}")

print("Where do you want to add the number?  (start/center/end)")
choice = input(": ").lower()  # converts the (input) value into lower case
element = int(input("Enter the number to add: "))

if choice == "start":
    array.insert(0, element)
elif choice == "center":
    center = len(array)/2
    array.insert(int(center), element)
elif choice == "end":
    array.append(element)
else:
    print("You entered the wrong input!")

print(f"Array: {array}")
print(f"Total elements in the list is: {len(array)}")
