x=eval(input())
for i in x:
    for n in range(2,i):
            if i%n==0:
                x.remove(i)
                break
            else:
                continue
print(x)
