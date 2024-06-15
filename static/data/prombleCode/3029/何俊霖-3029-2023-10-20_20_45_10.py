n=list(input().split(","))
s=list(input().split(","))
e=[]
for i in range(0,len(n)):
    e.append([n[i],int(s[i])])
print(e)
