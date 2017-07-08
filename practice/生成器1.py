

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1,2], [3,4],[5],[6]]
print list(flatten(nested))