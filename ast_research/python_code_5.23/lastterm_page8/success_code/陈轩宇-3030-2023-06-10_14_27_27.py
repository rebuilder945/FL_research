a = input().split(",")
b = eval(input())
c = []
for i in range(len(a)):
    d=[]
    d.append(a[i])
    d.append(b[i])
    c.append(d)
c.sort(key=b)
print(c)
    
