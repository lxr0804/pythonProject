def maopao(arrays):
    l = len(arrays)
    for i in range(l):
        for j in range(l - 1):
            if arrays[j] > arrays[j + 1]:
                arrays[j], arrays[j + 1] = arrays[j + 1], arrays[j]
    return arrays


print maopao([3, 5, 2, 8, 9, -3])
