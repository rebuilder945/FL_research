lst = list(eval(input()))
n,m = eval(input())
if -len(lst)<=n<=len(lst)-1:
    lst.append(lst[n])
    print(lst)
else:
    print("error")

