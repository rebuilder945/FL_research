lst1=eval(input())
n,m=map(int,input().split(','))
if 0<=n<=m<=len(lst1):
    del lst1[n:m]
    print(lst1)
else:
    print("error")    
