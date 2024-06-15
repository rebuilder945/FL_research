l=eval(input())
lst=list(l)
lst1=lst.copy()
n,m=eval(input())
for i in range(n,m):
    if i<=len(lst):
        lst1.remove(lst[i])
    else:
        print("error")
print(lst1)
