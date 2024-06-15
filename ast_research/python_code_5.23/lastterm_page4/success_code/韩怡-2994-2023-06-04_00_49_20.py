lst=input().split(',')
n,m=eval(input())
if n<len(lst):
    lst=lst+[lst[n]]*m
    lst=list(map(int,lst))
    print(lst)
else:
    print("error") 


