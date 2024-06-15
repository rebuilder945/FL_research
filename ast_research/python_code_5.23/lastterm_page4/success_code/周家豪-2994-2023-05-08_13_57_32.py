lst=input().split(",")
n,m=eval(input())
if n<-len(lst) or n>=len(lst):
    print('error')
else:
    lst2=[lst[n] for i in range(m)]
    print(list(map(int,lst+lst2)))
