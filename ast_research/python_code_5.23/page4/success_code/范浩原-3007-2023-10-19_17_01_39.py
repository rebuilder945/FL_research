lst=eval(input())
n,m=eval(input())
if n>len(lst)-1 or m>len(lst)-1:
    print("error")
else :
    if n>m:
       del lst[m:n]
    elif n<=m:
        del lst[n:m]
    print(lst)       
