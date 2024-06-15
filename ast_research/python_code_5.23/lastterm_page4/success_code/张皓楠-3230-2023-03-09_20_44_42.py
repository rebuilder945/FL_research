a = eval(input())
b = sorted(a)
b.reverse()
for i in b:
    if i == 0:
        print(0)
        break
    else:
        print(i,end='')
