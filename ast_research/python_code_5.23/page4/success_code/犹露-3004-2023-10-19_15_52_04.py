
a = eval(input())
m=[]
for i in a[:]:
    for n in range(2,i):
        if i%n==0:
            a.remove(i)
print(a)
