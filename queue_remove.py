# Python code to remove a number from a Queue data structure

q = [715470, 715471, 715473, 715474]
print(f"Queue: {q}")
print()

if len(q) == 0:
    print("Underflow!")
    print("Can't delete any elements from the queue!")
else:
    print("Do you want to delete an element? (yes/no)")
    choice = input(":").lower()  # lower(): converts the input into lowercase
    if choice == "yes":
        q.pop(0)
        # pop(0) eliminates the first element form a list
        print(f"Queue: {q}")
        print(f"Total number of elements in queue: {len(q)}")
    else:
        pass
