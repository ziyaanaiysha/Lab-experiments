
# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    elif key < root.data:
        return search(root.left, key)

    else:
        return search(root.right, key)


root = None

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display (Inorder)")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        data = int(input("Enter element: "))
        root = insert(root, data)
        print("Element inserted successfully")

    elif ch == 2:
        key = int(input("Enter element to search: "))

        if search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif ch == 3:
        print("Inorder Traversal:")
        inorder(root)
        print()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
