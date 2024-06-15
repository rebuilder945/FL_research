list1=eval(input())
n,m=eval(input())
list2=list1.copy()
if n  in list1 and m in list1:
    if n>m:
        for x in range(n,m):
            a=list1[x]
            del list2[a]
    else:
        for x in range(m,n):
            a=list1[x]
            del list2[a]
    print(list2)
else:
    print("error")
