a=input()
b=[]
for i in a:
    i=int(i)
    if (i+5)%10==0:
        b.insert(0,str(0))
        break
    else:
        i=(i+5)%10
        d=str(i)
        b.insert(0,d)
c=''.join(b)
print(c)


