lst=input().split()
n,m=input().split()
lst=list(lst)
n, m = int(n), int(m)
lst[int(n)], lst[int(m)] = lst[int(m)], lst[int(n)]
print(lst)
