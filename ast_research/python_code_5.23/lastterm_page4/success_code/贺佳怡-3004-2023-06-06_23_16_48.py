a=eval(input())
for i in a:
    for c in range(0,i):
        if i%c==0:
            a.remove(i)
print(a)

