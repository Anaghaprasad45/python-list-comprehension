def enumerate(l1):
    l2 = []
    for i in range(len(l1)):
        a = (i, l1[i])
        l2.append(a)
    return l2


print(enumerate(["a", "b", "c"]))
