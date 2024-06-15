lst = eval(input())
m = max(lst)
n = min(lst)
lst1 = lst.copy()
for i in lst:
    if i ==m or i == n:
        lst1.remove(i)
print(lst1)
