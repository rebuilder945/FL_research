a=input()
b=[]
for i in a:
    b.append((int(i)+5)%10)
b.reverse()
for x in range(len(b)):
    b[x]=str(b[x])
print(' '.join(b))
