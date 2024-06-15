lst=input()
n=eval(input())
m=eval(input())
for x in range(len(lst)):
    if n<=m:
        lst.remove(lst[n,m])
    else:
        print("error")
print(lst)
