lst=eval(input())
n,m=map(int,input().split(","))
lst2=[]
lst1=list(lst)
if n>=len(lst):
    print("error")
else:
    for i in range(len(lst)):
        if i==n:
            lst2.append(lst[i])
            lst2=lst2*m
            lst1.extend(lst2)
            break
    print(lst1)
