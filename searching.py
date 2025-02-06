array = ["J", "K", "L"]
array.sort()
print(array)

element = input("Which element's index do you want to find? : ").capitalize()
if element in array:
    index = array.index(element)
    print(f"{element} exists in index no {index}")
else:
    print("No element found")
