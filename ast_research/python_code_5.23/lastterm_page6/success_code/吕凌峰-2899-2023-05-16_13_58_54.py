#组合数字
def NumberCombine(x, y):
    if x < 0 or y < 0 or x > y or y - x < 3 or y > 9:
        print('illegal input')
    else:
        a = [i for i in range(x, y)]
        b = 0
        for i2 in range(len(a)):
            b += (pow(10, i2) * a[i2])
        b = str(b)
        Output = []
        for u in b:
            for v in b:
                if u == v or u == '0':
                    pass
                else:
                    for w in b:
                        if u == w or v == w:
                            pass
                        else:
                            Output.append(u+v+w)
        Output.sort(key=str.lower)
        print(' '.join(Output))
a, b = input().split(sep=' ')
a = int(a)
b = int(b)
NumberCombine(a, b)
