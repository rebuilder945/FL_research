lst=eval(input())
n,m=map(int,input().split(","))
if m<len(lst):
    for i in range(n,m):
        del lst[i]
        print(lst)
else:
    print("error")

