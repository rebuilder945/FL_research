lst=eval(input())
n,m=eval(input())
if n<=m and m > (len(lst)-1) :
    print("error")
else :
    del lst[n:m]
    print(lst)    
