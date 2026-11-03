
# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = None


def insert():
    global head

    data = int(input("Enter element: "))
    newnode = Node(data)

    if head is None:
        head = newnode
    else:
        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp

    print("Element inserted successfully")


def delete():
    global head

    if head is None:
        print("List is empty")
    else:
        temp = head
        print("Deleted element:", temp.data)

        head = head.next

        if head is not None:
            head.prev = None


def display():
    if head is None:
        print("List is empty")
    else:
        temp = head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


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
