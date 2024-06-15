str = input()
a,b = input().split()
lst = str.split()
a=int(a)
b=int(b)
temp = lst[a]
lst[a] = lst[b]
lst[b] = temp
print(lst)


