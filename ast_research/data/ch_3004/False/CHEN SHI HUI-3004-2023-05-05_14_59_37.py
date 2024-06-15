def ss(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
l=eval(input())
l1=list()
for x in l:
    if ss(x):
        l1.append(x)
print(l1)





