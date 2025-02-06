# Python code to remove a number from an array

array = [1, 2, 3, 4, 5, 5]
print(f"Array: {array}")

print("From where you want to remove the number: (start/center/end)")
choice = input(": ").lower()

if len(array) == 0:
    print("Array is empty! Can't remove any element.")

elif choice == "start":
    array.pop(0)
elif choice == "center":
    center = int(len(array) / 2)
    array.pop(center)
elif choice == "end":
    array.pop()
else:
    print("You entered the wrong input!")

print(f"Array: {array}")
print(f"Total elements in the array is: {len(array)}")
