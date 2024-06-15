a=eval(input())
b=[]
for i in a:
    isPrime = True
    for x in range(2,i):
        if i%x==0:
            isPrime = False
            break
    if isPrime:
        b.append(i)
b.remove(0)
b.remove(1)
print(b)
