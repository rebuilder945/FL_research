lst = list(eval(input()))
n,m = eval(input())
h = n + 1
if h > len(lst):
    print("error")
else:
    n = lst[n]
    for x in range(m):
        lst.append(n)
    print (lst)
