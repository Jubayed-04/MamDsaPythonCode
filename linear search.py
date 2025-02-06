# Python code for linear search

array = [1, 2, 3, 4, 5, 6]
data = 0
detect = int(input("Enter the item(you want to find): "))


for i in array:
    if i == detect:
        data = i
        break
if data == 0:
    print("Element not found")
else:
    print(f"{detect} found in the index no {array.index(data)}")
