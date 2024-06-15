lst=list(eval(input()))
n,m=eval(input())
if m<=len(lst) and n<=len(lst):
    for i in range(n,m):
        a=lst[i]
        lst.remove(a)
    print(lst)
else:
    print("error")
