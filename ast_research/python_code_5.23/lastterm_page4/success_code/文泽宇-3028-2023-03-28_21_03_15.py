n,m,l = eval(input())
k = n + l*(m-1)
lst = [x for x in range(n,k+1)]
lst1 = lst[::l]
print(lst1)
