# python program to sort a list

array = [1, 2, 3, 5, 4, 8, 7, 6]
print(f"Array: {array}")

print("In which order do you want to sort the array? (1:ascending/ 2:descending)")
choice = input(": ").lower()

if choice == "ascending" or choice == "1":
    print(f"Array: {sorted(array)}")
elif choice == "descending" or choice == "2":
    print(f"Array: {sorted(array, reverse=True)}")
else:
    pass
