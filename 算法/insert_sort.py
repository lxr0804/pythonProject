# A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# print A0

def insert_sort(list):
    count = len(list)
    for i in range(1, count):
        key = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1
    return list


list = [2, 1, 5, 5, 7, 2, 3, 9, 1, 0]
print insert_sort(list)
