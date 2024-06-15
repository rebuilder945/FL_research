sText = str(input()).split(' ')
n,m = eval(input())
lst = list(sText)
n = int(n)
m = int(m)
lst[n],lst[m] = lst[m],lst[n]
print(lst)
