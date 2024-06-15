n=input()
e=len(n)
d=''
for i in range(len(n)):
    c=n[i]
    c=int(c)
    a=(c+5)%10
    a=str(a)
    d+=a
d=list(d)
for i in range(len(n)//2):
    d[i],d[e-i-1]=d[e-i-1],d[i]

print(''.join(d))
