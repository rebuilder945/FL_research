list=input().split(",")
n,m=eval(input())
if n<m:
    del list[n,m]
    print(list)
if n>m:
    print("error")
elif n or m > len(list):
    print("error")

