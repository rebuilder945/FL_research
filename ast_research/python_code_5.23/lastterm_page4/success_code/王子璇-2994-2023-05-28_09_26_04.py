lst=list(eval(input()))
n,m=eval(input())
if n <= len(lst)-1 and n >= -len(lst):
    a=[lst[n]]*m
    lst=lst+a
    print(lst)
else:
    print('error')
