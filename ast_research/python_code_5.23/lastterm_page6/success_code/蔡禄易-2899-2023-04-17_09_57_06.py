n,m = input().split('')
n,m = int(n),int(m)
list1 = []
if type(n)!=int or type(m)!=int or n<0 or n>=10:
    list1 = []
else:
    for a in range(n,m):
        sa = str(a)
        for b in range(n,m):
            sb = str(b)
            for c in range(n,m):
                sc = str(c)
                s = sa+sb+sc
                if sa!=0 and sa!=sb and sb!=sc and sa!=sc and len(s)==3 and s not in list1:
                    list1.append(s)
if list1 == []:
    print("illegal input")
else:
    print(" ".join(x for x in list1))
