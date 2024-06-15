m=list(input())
print(m)
for x in range(len(m)):
    m[x]=(int(m[x])+5)%10
x=int(len(m)/2)
print(x)
print(m)
n=m[:x-1:-1]+m[:x:1]
s=""
for k in n:
    s=s+str(k)
print(s)
