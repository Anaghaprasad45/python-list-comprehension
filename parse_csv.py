def parse_csv(a):
    l1 = []
    f = open(a).readlines()
    for i in f:
        data = i.split()
        l1.append(data)
    return l1


print(parse_csv('sample.csv'))
