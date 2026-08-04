def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
numbers = [10, 25, 30, 45, 50]
key = 30
result = linear_search(numbers, key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")