n = eval(input())
a = [2,3]
b = [1,2]
for i in range(n+1):
    if n == 1:
        print('%.4f'%(2/1))
    elif n ==2:
        print('%.4f'%(2+3/2))
    else:
        ai = int(a[i-1])+int(a[i-2])
        a.append(ai)
        bi = int(b[i-1])+int(b[i-2])
        c = [2/1,3/2]
        c.append(a[i]/b[i])
