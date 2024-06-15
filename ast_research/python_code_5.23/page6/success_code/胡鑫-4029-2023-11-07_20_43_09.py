n,m = input().split()
list1 = []
list2 = []
if eval(m)-eval(n)<3:
    print("illegal input")
else:
    for i in range(eval(n),eval(m)):
        list1.append(i)
        for a in list1:
            for b in list1:
                for c in list1:
                    if a!=b and b!=c and c!=a:
                        list2.append((str(a)+str(b)+str(c)))
    print(*list2,sep=" ")

