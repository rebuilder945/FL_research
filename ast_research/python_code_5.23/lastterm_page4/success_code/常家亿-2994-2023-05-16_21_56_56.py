lst = input().split(",")
lst = list(map(int,lst))
n,m = eval(input())
w = len(lst)
if n < -w or n > w-1:
    print("error")
else:
    a = lst[n]
    b = [a]*m
    c = b.copy()
    for x in b:
        lst.append(x)
        c.remove(x)
    print(lst)
