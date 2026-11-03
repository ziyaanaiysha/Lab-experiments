
# Queue Using Array

queue = []

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        element = int(input("Enter element to insert: "))
        queue.append(element)
        print("Element inserted successfully")

    elif ch == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted element:", queue.pop(0))

    elif ch == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", queue)

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
