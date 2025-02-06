# Python code to add a number in a Queue Data structure

q = [715470, 715471, 715473, 715474]
print(f"Queue: {q}")

if len(q) >= 10:
    print("Overflow!")
    print("Can't add any element!")
else:
    print()  # to add a blank line
    add = int(input("Enter a number to add: "))
    q.append(add)
    print(f"Queue: {q}")
    print(f"Total number of elements in queue: {len(q)}")

# print("Front:", front := q[0])
# print("Rear:", rear := q[len(q)-1])
