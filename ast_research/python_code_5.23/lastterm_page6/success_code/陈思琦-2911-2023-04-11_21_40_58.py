a=input()
b=[]
for i in a:
    i=int(i)
    if (i+5)%10!=0:
        i=(i+5)%10
        d=str(i)
        b.insert(0,d)
    else:
        b.insert(0,0)
c=''.join(b)
print(int(c))


