dic={}
while True:
    s=input()
    if s =='q':
        break
    elif s in dic:
        dic[s]+=1
    elif s not in dic:
        dic[s]=0

n=0;name=None
for x in dic:
    if dic[x]>n:
        n=dic[x]
        name=x
print(name,n)
