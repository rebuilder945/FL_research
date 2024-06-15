lst1=input().split(",")
n,m=eval(input())
if n>len(lst1):
    print("error")
else:
    lst1=lst1+[lst1[n]]*m
    lst2=list(map(int,lst1))
    print(lst2)
    

