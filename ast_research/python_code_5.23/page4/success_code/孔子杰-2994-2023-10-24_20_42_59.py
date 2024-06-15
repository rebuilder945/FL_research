lst=input().split(",")
n,m=eval(input())
if n>len(lst) or n<-1-len(lst):
    print("error")
else:
    str=lst[n]*m
    lst1=list(str)
    lst2=lst+lst1
    print(lst2)
