
a = eval(input())
m=[]
for i in a[:]:
    for n in range(2,i):
        if i%n==0:
            if i in a:
                a.remove(i)
            else:
                pass
print(a)
