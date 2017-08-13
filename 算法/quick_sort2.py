def quick(args):
    if not args:
        return []
    small_list = []
    big_list = []
    middle = args[0]

    for i in args[1:]:
        if i <= middle:
            small_list.append(i)
        else:
            big_list.append(i)

    return quick(small_list) + [middle] + quick(big_list)


args = [2, 4, 1, 7, 2, 1, 6, 3]

print quick(args)[-2]
