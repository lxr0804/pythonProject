def quicksort(arr):
    if not arr:
        return []
    small = []
    big = []
    key = arr[0]
    for i in arr[1:]:
        if i <= key:
            small.append(i)
        else:
            big.append(i)
    return quicksort(small) + [key] + quicksort(big)


arr = [1, 2, 4, 56, 1, 2, 4, 5, 6, 0]
print quicksort(arr)
