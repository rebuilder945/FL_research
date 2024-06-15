a = eval(input())
b = sorted(a)
b.reverse()
for i in b[:-1]:
    if not i == 0:
        break
    del b[0]
for i in b:
    print(i,end='')
