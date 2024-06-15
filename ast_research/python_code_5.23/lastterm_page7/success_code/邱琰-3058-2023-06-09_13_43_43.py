dic={}
while 1:
    n=input()
    if n=='q':
        break
    if n not in dic:
        dic[n]=1
    else:
        dic[n]+=1
m=0
s=''
for i in dic:
    if dic[i]>=m:
        m=dic[i]
        s=i
print(s,m)
