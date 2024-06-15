lst=list(eval(input()))
n,m=eval(input())
if m-1<=len(lst):
    for i in range(n,m):
        a=lst[i]
        lst.remove(a)
    print(lst)
elif m-1>len(lst):
    print("error")
