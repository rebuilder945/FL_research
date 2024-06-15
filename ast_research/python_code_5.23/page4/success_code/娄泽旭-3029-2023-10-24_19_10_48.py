a = list(input())
b = input()
c = int(a.count())
d = [[a[i],b[i]] for i in range(c)]
print(d)
