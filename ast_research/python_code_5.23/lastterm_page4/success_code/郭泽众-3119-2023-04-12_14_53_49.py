lst = eval(input())
[lst.remove(i) for i in lst[::-1] if lst.count(i) > 1]
print(lst)
