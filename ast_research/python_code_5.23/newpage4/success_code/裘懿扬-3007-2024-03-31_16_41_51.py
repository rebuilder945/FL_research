lst=list(eval(input()))
n,m=eval(input())
if m<=len(lst):
    for i in range(n,m):
        a=lst[i]
        lst.remove(a)
    print(lst)
elif m>len(lst):
    print("error")
