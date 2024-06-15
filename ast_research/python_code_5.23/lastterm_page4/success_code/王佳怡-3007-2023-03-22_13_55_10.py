l=eval(input())
lst=list(l)
n,m=eval(input())
for i in range(n,m):
    if i<=len(lst):
        lst.remove(lst[i])
    else:
        print("error")
print(lst)


