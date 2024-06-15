s=input()
s1=[]
s2=[]
ls=[]
for i in s:
    if i.isdigit():
        s1.append(i)
        s2.append(s1)
    if i.isalpha():
        s1=[]
s3=[s2[i] for i in range(len(s2)-1,-1,-1)]
for j in s3:
    m=len(j)
    ls.append(m)
ls.sort()
max=int(ls[-1])
for x in s3:
    if len(x)==max:
        print(''.join(x))
        break
