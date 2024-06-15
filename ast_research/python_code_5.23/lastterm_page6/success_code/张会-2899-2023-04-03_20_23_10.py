n,m = map(int,input().split())
l1 = []
l2 = []
if 0<= n < m <11 and m-n>=3:
    for z in range(n,m):
        l1.append(z)
    for i in range(len(l1)):
        for x in range(len(l1)):
            for y in range(len(l1)):
                if i != x and x != y and y != i:
                    s2 = str(l1[i])+str(l1[x])+str(l1[y])
                    if s2 not in l2:
                        l2.append(s2)
                    else:
                        pass
                else:
                        pass
    for a in l2:
        a =int(a)
        if a > 99:
            print('%d '%a,end='')
else:
    print('illegal input')
