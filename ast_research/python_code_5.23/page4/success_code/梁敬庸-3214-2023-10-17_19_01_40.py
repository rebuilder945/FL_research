a=eval(input())
b=[]
for x in a:
    if x!=0:
        b.append(x)
c=len(a)-len(b)
for i in range(c):
    b.append(0)
print(b)
