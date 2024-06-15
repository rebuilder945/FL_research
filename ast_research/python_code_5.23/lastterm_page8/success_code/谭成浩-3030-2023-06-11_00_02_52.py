n=list(input().split(','))
m=list(input().split(','))
c1=[]
for i in range(len(n)):
    c=[]
    c.append(n[i])
    c.append(eval(m[i]))
    c1.append(c)
def zai(n):
    return n[1]
c1.sort(key=zai)
print(c1)
