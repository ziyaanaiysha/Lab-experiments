
# Circular Queue Using Array

SIZE = 5
queue = [None] * SIZE

front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        if (rear + 1) % SIZE == front:
            print("Queue Overflow")

        else:
            element = int(input("Enter element: "))

            if front == -1:
                front = 0

            rear = (rear + 1) % SIZE
            queue[rear] = element

            print("Element inserted successfully")

    elif ch == 2:
        if front == -1:
            print("Queue Underflow")

        else:
            print("Deleted element:", queue[front])
            queue[front] = None

            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % SIZE

    elif ch == 3:
        if front == -1:
            print("Queue is empty")

        else:
            print("Queue elements:")
            i = front

            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % SIZE

            print()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
