def names(n):
    y = n[0].upper() + n[1:].lower()
    return y


print map(names, ['MicHael', 'Sarah', 'Tracy', 'Bob', 'Jack'])
