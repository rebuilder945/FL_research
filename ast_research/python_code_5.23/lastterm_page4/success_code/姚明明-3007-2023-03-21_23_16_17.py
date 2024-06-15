lst=[]
n,m=map(int,input().split(","))
if n<=m and m>=len(lst)//2:
    del lst[n:m]
    print(lst)
else:
    print("error")
