
# Stack Using Array

stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        element = int(input("Enter element to push: "))
        stack.append(element)
        print("Element inserted successfully")

    elif ch == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Deleted element:", stack.pop())

    elif ch == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", stack[::-1])

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
