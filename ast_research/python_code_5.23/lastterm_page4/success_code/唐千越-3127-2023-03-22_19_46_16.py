n=eval(input())
lst=range(1,n+1)
lstnew=[]
for i in range(n-1):
    lstnew.append(lst[i+1])
lstnew.append(lst[0])
print(lstnew)
