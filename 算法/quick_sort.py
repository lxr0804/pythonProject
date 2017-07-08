def quick_sort(arrays, lower, upper):
    if lower < upper:
        key = arrays[lower]
        i = lower
        j = upper
        while i < j:
            while i < j and a[j] >= key:
                j -= 1
            a[i], a[j] = a[j], a[i]
            while i < j and a[i] < key:
                i += 1
            a[i], a[j] = a[j], a[i]
        # arrays[j] = key
        quick_sort(arrays, lower, i - 1)
        quick_sort(arrays, i + 1, upper)


a = [3, 1, 2, 3, 4, 5]

quick_sort(a, 0, len(a) - 1)

print a
