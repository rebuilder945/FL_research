lst=[]
n,m=eval(input().split(','))
if n<=m and m<=len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")
