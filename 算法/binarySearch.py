# encoding=utf-8



def search(arrays, target, lower, upper):
    if lower == upper:
        if arrays[upper] == target:
            return upper
        else:
            return -1
    else:
        middle = (lower + upper) / 2
        if arrays[middle] > target:
            return search(arrays, target, lower, middle)
        elif arrays[middle] < target:
            return search(arrays, target, middle + 1, upper)
        else:
            return middle

arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

print search(arrays, target, 0, len(arrays)-1)
