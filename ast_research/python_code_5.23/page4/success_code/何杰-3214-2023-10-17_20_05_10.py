n=eval(input())
i=0
while i<len(n):
    a=n[i]
    if a==0:
        n.remove(0)
        n.append(0)
    i+=1
print(n)

