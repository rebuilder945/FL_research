lst=eval(input())
n,m=eval(input())
a=[]
if n<=len(lst)-1:
    a.append(lst[n])
    lst1=lst+a*m
    print(lst1)
else:
    print("error")
