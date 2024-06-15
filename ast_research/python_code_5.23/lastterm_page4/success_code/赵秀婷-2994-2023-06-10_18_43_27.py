lst=list(map(int,input().split(",")))
n,m=eval(input())
if n>len(lst) or n<-len(lst):
    print("error")
else:
    temp=[lst[n]*m]
    print(lst+temp)
