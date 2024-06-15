lst=[]
n,m=int(input().split(','))
if n<=m and m>=len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")
