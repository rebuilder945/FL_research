lst1=list(eval(input()))
n,m=eval(input())
if n>=len(lst1) or n<-1*len(lst1):
    print("error")
else:
    lst2=[lst1[n]]*m
    lst3=lst1+lst2
    print(lst3)
