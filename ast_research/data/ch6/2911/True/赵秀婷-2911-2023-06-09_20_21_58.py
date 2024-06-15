num=list(map(int,input()))
c=[]
for x in num:
    x=str((int(x)+5)%10)
    c.append(x)
c.reverse()
print(''.join(c))
