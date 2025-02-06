# Python code for binary search

array = [1, 2, 3, 4, 6, 7, 8, 8]
print(array)
loc = 0
item = int(input("Enter an item to find out: "))

while True:
    mid = round(len(array) / 2)
    if array[mid] == item:
        loc = 1
        break
    else:
        if item > array[len(array)-1] or item < array[0]:
            break
        elif array[mid] > item:
            for i in range(len(array), mid, -1):
                array.pop()
        else:
            for i in range(0, mid):
                array.pop(i)

print("Item found!") if loc != 0 else print("item not found!")
