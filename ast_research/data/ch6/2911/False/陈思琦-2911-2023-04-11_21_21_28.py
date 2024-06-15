a=input()
b=[]
for i in a:
    i=int(i)
    i=(i+5)%10
    d=str(i)
    b.insert(0,d)
c=''.join(b)
print(int(c))

