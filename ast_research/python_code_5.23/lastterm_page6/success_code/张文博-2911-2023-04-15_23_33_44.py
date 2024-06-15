m=list(input())

for x in range(len(m)):
    m[x]=(int(m[x])+5)%10
n=m[::-1]
s=""
for k in n:
    s=s+str(k)
print(s)
