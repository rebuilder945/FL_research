dic={}
while True:
    s=input()
    if s=='q':
        break
    if s in dic:
        dic[s]+=1
    if s not in dic:
        dic[s]=1

n=0;name=None
for x in dic:
    if dic[x]>n:
        n=dic[x]
        name=x
print(name,n)
