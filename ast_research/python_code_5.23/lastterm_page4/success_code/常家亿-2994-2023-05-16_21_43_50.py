lst = input().split(",")
lst = list(map(int,lst))
n,m = eval(input())
if lst[n] not in lst:
    print("error")
else:
    a = lst[n]
b = [a]*m
c = b.copy()
for x in b:
    lst.append(x)
    c.remove(x)
print(lst)