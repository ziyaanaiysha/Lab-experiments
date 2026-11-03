
# Binary Search

a = list(map(int, input("Enter array elements: ").split()))

a.sort()

print("Sorted array:", a)

key = int(input("Enter element to search: "))

low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break

    elif a[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element not found")

