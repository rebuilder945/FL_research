[n,m] = input().split()
b = []
sum1 = []
for x in range(n,m):
    if n<m and m-n>2:
        b.append(x)
        for i in range(len(b)): 
            for y in range(len(b)):
                for z in range(len(b)):
                    if i!= y and i!=z and z!=y and b[i]!=0:
                        s1 = str(b[i])+str(b[y])+str(b[z])
                        if s1 not in sum1:
                            sum1.append(s1)
                        else:
                            pass
                    else:
                        pass
    else:
        print('illegal input')
print(m)
