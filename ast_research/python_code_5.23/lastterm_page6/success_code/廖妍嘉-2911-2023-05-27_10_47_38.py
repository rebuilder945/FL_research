lst=list(input())
for i in range(len(lst)):
    lst[i]=(int(lst[i])+5)%10
    lst.reverse()
    lst2=[str(i) for i in lst]
    num=int(''.join(lst2))
print((num))
