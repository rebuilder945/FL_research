a=list((int,input().split(",")))
b,c=eval(input())
d=a[b]
for x in range(c):
    a.append(d)
print(a)
