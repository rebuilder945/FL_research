lst=eval(input())
n,m=eval(input())
if m>(len(lst)-1):
    print("error")
else:
    for i in range(n,m):
        del lst[i]
print(lst)
