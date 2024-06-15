ls1 = input().split(',')
ls2 = list(map(int, input()[1:-1].split(',')))
ls3 = [[x, y] for x, y in zip(ls1, ls2)]
print(ls3)
