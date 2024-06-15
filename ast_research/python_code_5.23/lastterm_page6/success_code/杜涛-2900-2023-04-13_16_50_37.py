n=eval(input())
if n<=2 or n-int(n)!=0:
    print("illegal input")
else:
    lst=[]
    for i in range(2,n):
        a=1
        for j in range(2,i):
            if i%j==0:
                a=0
        if a==1:
            lst.append(i)
    lst1=list(map(str,lst))
    lst2=[]
    for i in range(len(lst1)):
        if lst1[i][::-1]==lst1[i]:
            lst2.append(lst1[i])
    lst3=list(map(eval,lst2))
    for x in lst3:
        print("%d"%(x),end=" ")

