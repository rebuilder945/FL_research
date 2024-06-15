a = list(input().split(","))
b = eval(input())
c = []
for i in range(0,len(a)):
    c.append([a[i],int(b[i])])
print(c)
