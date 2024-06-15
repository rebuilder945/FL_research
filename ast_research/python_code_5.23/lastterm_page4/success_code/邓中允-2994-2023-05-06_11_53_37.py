lst=list(eval(input()))
n,m=eval(input())

if n>len(lst):
    print("error")
else:
    c=[lst[n]]*m
    b=lst+c
    print(b)

