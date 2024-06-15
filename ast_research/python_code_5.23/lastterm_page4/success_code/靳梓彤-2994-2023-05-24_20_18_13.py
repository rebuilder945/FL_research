lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst) or n<-1*len(lst):
    print("error")
else:
    a=lst[n]
    a1=[a]*m
    lst=lst+a1
    print(lst)
