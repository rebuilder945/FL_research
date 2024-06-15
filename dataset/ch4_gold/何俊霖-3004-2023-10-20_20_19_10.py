from os import remove


x=eval(input())
for i in x:
    for n in range(2,i):
        if i%n==0:
            if i in x:
                x.remove(i)
    if i==1:
        x.remove(i)
print(x)

