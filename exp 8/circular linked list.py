
# Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


last = None


def insert():
    global last

    data = int(input("Enter element: "))
    newnode = Node(data)

    if last is None:
        last = newnode
        newnode.next = newnode
    else:
        newnode.next = last.next
        last.next = newnode
        last = newnode

    print("Element inserted successfully")


def delete():
    global last

    if last is None:
        print("List is empty")
        return

    temp = last.next

    if temp == last:
        last = None
    else:
        last.next = temp.next

    print("Deleted element:", temp.data)


def display():
    if last is None:
        print("List is empty")
        return

    temp = last.next

    while True:
        print(temp.data, end=" -> ")
        temp = temp.next

        if temp == last.next:
            break

    print("(Back to first node)")


while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        insert()

    elif ch == 2:
        delete()

    elif ch == 3:
        display()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
