n=list(input().split(","))
s=eval(input())
e=[]
for i in range(0,len(n)):
    e.append([n[i],int(s[i])])
print(e)
