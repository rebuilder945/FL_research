a=input()
lst=list(a.split(','))
n, m = input().split()
n=int(n)
m=int(m)
lst[n], lst[m] = lst[m], lst[n]
print(lst)
