lst = list(eval(input()))
n,m = eval(input())
if -len(lst) < n <len(lst)-1:
    for i in range(m):
        a = lst[n]
        lst.append(a)
    print(lst)
else:
    print("error")

