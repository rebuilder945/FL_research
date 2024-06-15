a = tuple((input().split(",")))
c = list(a)
b = eval(input())
M = []
for i in range(len(a)):
    d = [a[i],b[i]]
    M.append(d)


print(M)
