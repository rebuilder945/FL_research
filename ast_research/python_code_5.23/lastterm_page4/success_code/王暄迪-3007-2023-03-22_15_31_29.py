lst=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
if n<len(lst) and m<len(lst):
        del lst[n:m]
        print(lst)
else:
    print("error")
