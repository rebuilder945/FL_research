a=list(input().split(" "))
b,c=eval(input().split(" "))
a[b] = a[c]
a[c] = a[b]
print(a)
