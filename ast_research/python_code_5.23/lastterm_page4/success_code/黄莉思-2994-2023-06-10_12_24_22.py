lst=list(eval(input()))
n,m=eval(input())
a=len(lst)-1
b=len(lst)*(-1)
ls=[]
if 0<=n<=a or b<=n<0:
    ls.append(lst[n])
    ls=ls*m
    lst=lst+ls
    print(lst)
else:
    print("error")
    
