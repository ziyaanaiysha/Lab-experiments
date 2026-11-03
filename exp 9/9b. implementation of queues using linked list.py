
# Queue Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


front = None
rear = None


def enqueue():
    global front, rear

    data = int(input("Enter element: "))
    newnode = Node(data)

    if front is None:
        front = rear = newnode
    else:
        rear.next = newnode
        rear = newnode

    print("Element inserted successfully")


def dequeue():
    global front, rear

    if front is None:
        print("Queue Underflow")
    else:
        print("Deleted element:", front.data)
        front = front.next

        if front is None:
            rear = None


def display():
    if front is None:
        print("Queue is empty")
    else:
        temp = front

        print("Queue elements:")

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        enqueue()

    elif ch == 2:
        dequeue()

    elif ch == 3:
        display()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
