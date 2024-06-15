b=[]
while True:
    a=input()
    if a=="#":
        break
    b.append(a)
m=len(b)
for i in range(len(b)):
    b[i]=int(b[i])
print(m,sum(b))
