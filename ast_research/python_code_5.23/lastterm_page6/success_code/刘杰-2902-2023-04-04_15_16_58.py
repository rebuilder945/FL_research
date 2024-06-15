n = int(input())
list=[]
x=2
y=1
i=1
while i <= n:
    list.append(float(x/y))
    x = y + x  
    y = x - y
    i = i + 1
s=float(sum(list))
print("%.4f" % (s))
