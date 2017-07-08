def search(seq, number, lower, upper):
    if lower == upper and number == seq[upper]:
        return upper
    else:
        middle = (lower + upper) // 2
        if number > seq[middle]:
            return search(seq, number, middle + 1, upper)
        else:
            return search(seq, number, lower, middle)


seq = range(1, 100)
print search(seq, 66, 0, 99)
