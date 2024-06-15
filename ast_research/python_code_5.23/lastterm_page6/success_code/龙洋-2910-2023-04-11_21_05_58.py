h=eval(input())
n=eval(input())
l=h
s=0
for x in range(n):
    s=s+2*l
    l=l*0.5
s=s-h
print("%.2f"%s)
