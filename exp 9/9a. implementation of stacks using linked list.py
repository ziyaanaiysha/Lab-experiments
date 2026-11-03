
# Stack Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None


def push():
    global top

    data = int(input("Enter element: "))
    newnode = Node(data)

    newnode.next = top
    top = newnode

    print("Element inserted successfully")


def pop():
    global top

    if top is None:
        print("Stack Underflow")
    else:
        print("Deleted element:", top.data)
        top = top.next


def display():
    if top is None:
        print("Stack is empty")
    else:
        temp = top

        print("Stack elements:")

        while temp is not None:
            print(temp.data)
            temp = temp.next


while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        push()

    elif ch == 2:
        pop()

    elif ch == 3:
        display()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
