# coding=utf-8

def quick_sort(args, low, high):
    key = args[low]
    i = low
    j = high
    while i < j:
        while i < j and args[j] >= key:
            j -= 1
        args[i], args[j] = args[j], args[i]
        while i < j and args[i] < key:
            i += 1
        args[i], args[j] = args[j], args[i]
        quick_sort(args, low, i - 1)
        quick_sort(args, i + 1, high)


args = [1, 26, 2, 4, 7, 3, 6, 7, 3, 8, 0]
quick_sort(args, 0, len(args) - 1)

print args
