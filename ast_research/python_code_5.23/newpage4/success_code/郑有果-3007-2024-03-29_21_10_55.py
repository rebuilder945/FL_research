lst=eval(input())
n,m=eval(input())
a=list(lst[i] for i in range(n,m))
for i in range(n,m):
    if a:
       del lst[i]
    else:
        print("error")
print(lst)

