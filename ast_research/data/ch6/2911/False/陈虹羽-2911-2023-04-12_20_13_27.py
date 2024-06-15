n=input()
t=''
c=''
for i in n:
    i=int(i)
    i+=5
    i=i%10
    i=str(i)
    t+=i
t=list(t)
t[0],t[-1]=t[-1],t[0]
for i in t:
    c+=i
print(c)


