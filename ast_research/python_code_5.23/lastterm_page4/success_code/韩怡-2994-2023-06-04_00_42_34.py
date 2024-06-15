lst1=input().split(",")
n,m=eval(input())
if n>len(lst1):
    print("error")
else:
    t=lst1[n]
    s=t*m
    lst2=lst1+s
    lst3=list(map(int,lst2))
    print(lst2)
    

