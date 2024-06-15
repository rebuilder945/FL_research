lst= input().split(',') 
n,m=map(int,input().split(","))
a=len(lst)
a=lst[n]
if n>=a:
    print("error")
else:
    for i in range(m):
        lst.append(a)
    print(lst)


