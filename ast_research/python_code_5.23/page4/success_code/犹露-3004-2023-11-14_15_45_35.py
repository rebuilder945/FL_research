
a = eval(input())
m=[]
if 1 in a:
    a.remove(1)
if 0 in a:
    a.remove(0)
    
for i in a[:]:
    for n in range(2,i):
        if i%n==0:
            if i in a:
                a.remove(i)
            else:
                pass
print(a)
