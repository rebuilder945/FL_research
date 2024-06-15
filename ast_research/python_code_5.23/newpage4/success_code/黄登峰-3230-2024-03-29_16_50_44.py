a=eval(input())
a1=sorted(a,reverse=True)
y=""
for i in a1:
    x=str(i)
    y=y+x
if y[0]==0:
    y=0
print(y)
