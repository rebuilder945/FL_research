n = input()
a = [i for i in range(1,n+1)]
b = a[0]
for i in range(0,len(a)-1):
    a[i] = a[i+1]
a[-1] = b
print(a)
