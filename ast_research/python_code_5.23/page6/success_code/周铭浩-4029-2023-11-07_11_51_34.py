import random
ls=list(input().split(' '))
n=int(ls[0])
m=int(ls[1])
if m-n<3:
    print('illegal input')
ls1=[str(x) for x in range(n,m)]
ls2=[]
ls3=[]
for x in range(len(ls1)):
    ls2.append(ls1[x])
    for y in range(x+1,len(ls1)):
        ls2.append(ls1[y])
        for z in range(y+1,len(ls1)):
            ls2.append(ls1[z])
            str1=''.join(ls2)
            ls3.append(str1)
            ls2.pop(-1)
            if z==len(ls1):
                ls2.pop(-1)
            if y==len(ls1):
                ls2.clear()
set1=list(set(ls3))
for x in range(len(set1)):
    str2=set1[x]
    a=[]
    for y in range(len(str2)):
        a.append(str2[y])
    b=[]
    for i in range(100000):
        random.shuffle(a)
        b.append(''.join(a))
        c=list(set(b))
ls4=[int(x) for x in c]
for i in range(len(ls4)):
    print(ls4[i],end=' ')



