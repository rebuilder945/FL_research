a=eval(input())
b=[]
for x in range(len(a)-1,-1,-1):
    if x not in b:
        b.append(x)
c=b.reverse
print(c)
