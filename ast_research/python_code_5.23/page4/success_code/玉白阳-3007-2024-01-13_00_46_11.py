def del_(list,n,m):
    if n<0 or m>=len(list) or n>=len(list):
        print("error")
    else:
        del list[n:m]
        print(list)

list=eval(input())
a=input().split(",")
n=int(a[0])
m=int(a[1])
del_(list,n,m)
