list = eval(input())
E = []
N = E.copy()
for a in 'abcdefghijklmnopqrstuvwxyz':
    for x in list:
        for y in x:
            if y == a:
                if y not in E:
                    N1 = E.copy()
                    N1.clear()
                    for z in list:
                        N1.append(z.count(y))
                    N.append(y+','+str(sum(N1)))
                    E.append(y)
for i in N:
    print(i)
