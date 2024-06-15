lst = input().split()
s = list(map(int,input().split()))
n = s[0]
m = s[1]
lst1 = lst[:]
lst[n] = lst[m]
lst[m] = lst1[n]
print(lst)
