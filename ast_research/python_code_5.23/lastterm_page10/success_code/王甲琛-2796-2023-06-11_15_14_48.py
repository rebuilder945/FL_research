a=input()
b=0
ls1=[]
ls2=[]
for i in a:
    if i.isdigit()==True:
        ls1.append(str(i))
        if len(ls1)>=b:
            b=len(ls1)
            ls2.extend([ls1])
    else:
        ls1=[]

for x in range(len(ls2[-1])):
    ls2[-1][x]=str(ls2[-1][x])
c=''.join(ls2[-1])
if b==0:
    print('No digits')
else:
    print(c)
