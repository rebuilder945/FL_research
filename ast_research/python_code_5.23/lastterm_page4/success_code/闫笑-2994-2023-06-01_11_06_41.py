lst=input().split(',')
n,m=input().split(',')
n=int(n)
m=int(m)
if n<len(lst):
    lst=lst+[lst[n]]*m
    lst=list(map(int,lst))
    print(lst)
if n>len(lst):
    print("error") 

