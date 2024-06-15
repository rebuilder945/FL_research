A = eval(input())
B = {}
for x in A:
    for i in x:
        if i not in B:
            B[i]=1
        else:
            B[i] += 1
B = sorted(B.items(),key = lambda x:x[0])
B = [list(x) for x in B]
for i in B:
    print("%s,%d"%(i[0],i[1]))
