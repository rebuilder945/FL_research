lst = eval(input())
n, m = eval(input())
if n > m:
    n, m = m, n
else:
    n,m = n,m
if m > len(lst):
    print("error")
else:
    for i in range(m,n,-1):
        lst.remove(lst[i-1])
    print(lst)  
