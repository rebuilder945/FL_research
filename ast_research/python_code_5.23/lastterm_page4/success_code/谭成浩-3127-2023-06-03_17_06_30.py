n=eval(input())
lst=[]
if n==2:
    print([2,1])
else:
    for i in range(2,n+1):
        lst.append(i)
    lst.append(1)
    print(lst)
