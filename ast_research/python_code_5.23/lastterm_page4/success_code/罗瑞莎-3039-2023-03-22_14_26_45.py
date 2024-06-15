lst = eval(input())
m = max(lst)
n = min(lst)
for i in lst:
    if i ==m or i == n:
        lst.remove(i)
print(lst)
