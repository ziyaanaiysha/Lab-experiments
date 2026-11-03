
# Quick Sort

def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[-1]

    left = []
    right = []

    for i in a[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


a = list(map(int, input("Enter array elements: ").split()))

result = quick_sort(a)

print("Sorted array:", result)
