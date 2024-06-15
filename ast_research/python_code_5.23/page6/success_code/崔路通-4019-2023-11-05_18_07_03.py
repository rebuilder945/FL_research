a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
b=[(x+5)%10 for x in b ]
c=b.copy()
if len(c)%2==0:
    for i in range(len(c)/2):
        b[i],b[len(c)-1-i]=b[len(c)-1-i],b[i]
else:
    for i in range((len(c)-1)/2):
        b[i],b[len(c)-1-i]=b[len(c)-1-i],b[i]
d="".join(b)
print(d)




