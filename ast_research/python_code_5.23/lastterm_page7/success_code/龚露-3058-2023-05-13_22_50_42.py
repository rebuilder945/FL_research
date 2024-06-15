a = input()
i=0
num=[]
while i >= 0:
    if a =='q':
        break
    else:
        i = i+1
        num.append(a)
        a=input()
b={}
ls=[]
for i in num:
    b[i] = b.get(i,0)+1
for k,v in b.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1])
m,n=ls[-1]
print(m,n)
