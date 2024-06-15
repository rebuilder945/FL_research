l=eval(input())
lst=list(l)
n,m=eval(input())
for i in range(n,m):
    if i in int(len(lst)):
        lst.remove(lst[i])
    else:
        print("error")
print(lst)


