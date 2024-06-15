lst=eval(input())
n,m=eval(input())
if n and m<=len(lst)-1:
    for i in range(n,m):
        del lst[i]
        print(lst)
else:
    print("error")
