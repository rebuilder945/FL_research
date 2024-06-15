def issu(num):
    for i in range(2,num):
        if num%i==0:
            return False
        return True
b=eval(input())
if 0 in b:
    b.remove(0)
if 1 in b:
    b.remove(1)
a=[]
for i in b:
    if issu(i):
        a.append(i)
print(a)

