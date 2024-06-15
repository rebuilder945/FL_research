lst = list(eval(input()))
lst2 = lst.copy()
n,m = eval(input())
if n > len(lst):
    print("error")
else:
    for i in range(m):
        a = lst[n]
        lst2.append(a)
    print(lst2)
