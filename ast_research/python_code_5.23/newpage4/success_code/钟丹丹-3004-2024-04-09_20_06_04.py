n=eval(input())
for x in n:
    for i in range(2,x//2+1):
        if x%i==0:
            n.remove(x)
print(n)
