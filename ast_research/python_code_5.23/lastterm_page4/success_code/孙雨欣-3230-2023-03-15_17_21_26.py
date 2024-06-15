ls1=eval(input())
b=0
while len(ls1)>0:
    a=max(ls1)
    b=b*10+a
    ls1.remove(a)
print(b)
