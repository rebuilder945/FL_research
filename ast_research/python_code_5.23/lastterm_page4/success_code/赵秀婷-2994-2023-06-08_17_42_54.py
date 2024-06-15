lst=list(map(int,input.split(",")))
n,m=eval(input())
if n>len(lst) or n<-len(lst):
    print("error")
else:
    temp=[lst[n] for i in range(0,m)]
    print(lst+temp)
