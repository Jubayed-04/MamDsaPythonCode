# Python code for Bubble sorting

array = [2, 5, 6, 2, 4, 21, 11, 23, 44, 9, 55, 666, 1, 3, 4]
n = len(array)
print(array)

for i in range(1, n-1):
    ptr = 0
    while ptr < n-i:
        if array[ptr] > array[ptr+1]:
            temp = array[ptr]
            array[ptr] = array[ptr+1]
            array[ptr+1] = temp
        ptr += 1
print("Sorted array:\n", array)
