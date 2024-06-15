list=input().split(",")
n,m=eval(input())
if n<m:
    t=list.pop(n,m)
    print(t)
if n>m:
    print("error")
elif n or m > len(list):
    print("error")

