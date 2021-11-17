def triplets(n):
    l1 = []
    for i in range(1, n):
        for j in range(i, n):
            for m in range(j, n):
                if i+j == m:
                    l1.append((i, j, i+j))
    return l1


print(triplets(5))
