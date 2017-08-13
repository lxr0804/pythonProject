# coding=utf-8
def search(arr, lower, upper, tar):
    if lower == upper:
        if tar == arr[upper]:
            return upper
        else:
            return -1
    else:
        mid = (lower + upper) / 2
        if tar > arr[mid]:
            return search(arr, mid+1, upper, tar)
        elif tar < arr[mid]:
            return search(arr, lower, mid, tar)
        else:
            return mid


print search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 6)
