x=1
y=2
n=eval(input())
s=0
for i in range(0,n):
    z=y/x
    y=y+x
    x=y
    s=s+z
print("%.4f")%s
