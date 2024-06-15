a=eval(input())
b=list(str(a))
c=[int(i) for i in b]
e=[]


for i in range(len(c)):
    d=(c[i]+5)%10
    e.append(d)
print(e)
for i in range(len(e)//2):
    e[i],e[len(e)-1-i]=e[len(e)-1-i],e[i]
f=""
for i in e:
    f+=str(i)+""
print("".join(f))
