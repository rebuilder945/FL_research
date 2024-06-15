n = int(input())
if n<=0:
    print("illegal input")
elif (float(n)-int(n))>0:
    print("illegal input")
else:
    lst = []
    for i in range(n):
        if i>=2:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                lst.append(i)
    lst1 = list(map(str,lst))
    lst2 = []
    for k in lst1:
        if k == k[::-1]:
            lst2.append(k)
    print(" ".join(lst2))
