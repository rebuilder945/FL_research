n=input().split(",")
s=input().split(",")
b=[]
for i in range(len(n)):
    a=[]
    a.append(n[i])
    a.append(s[i])
    b.append(a)
b.sort(key=lambda x:x[1])
print(b)

