lst=eval(input())
n,m=map(int,input().split(","))
a=len(lst)
if n>=a:
    print("error")
else:
    for i in range(m):
        lst.append(lst[n])
print(lst)


