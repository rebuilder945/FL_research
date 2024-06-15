a = list(input().split(","))
b = list(eval(input()))
d = list([a[i],b[i]] for i in range(len(a)))
print(d)
