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
b=len(t)
for i in range(b//2):
    t[i],t[-1-i]=t[-1-i],t[i]
for i in t:
    c+=i
print(c)


