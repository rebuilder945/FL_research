n = eval(input())
m = 0
lst = [m+1 for m in range(0,n)]
a = lst.pop(0)
lst.append(a)
print(lst)
