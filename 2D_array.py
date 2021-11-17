def array(a, b):
    arr1 = []
    for i in range(a):
        arr2 = []
        for j in range(b):
            arr2.append(None)
        arr1.append(arr2)
    arr1[0][0] = 2
    return arr1


print(array(2, 3))
