lst1=input().split(",")
n,m=eval(input())
if n>len(lst1):
    print("error")
else:
    t=lst1[n]
    s=t*m
    lst2=str(lst1)+str(s)
    lst3=list(map(int,lst2))
    print(lst2)
    

