lst=list(eval(input()))
n,m=eval(input())
c=lst[n]*m
if n>len(lst):
    print("error")
else:
    b=lst+c
    print(b)

