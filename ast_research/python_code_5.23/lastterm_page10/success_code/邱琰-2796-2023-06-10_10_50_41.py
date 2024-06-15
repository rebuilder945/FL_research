n=list(input())
ls=[]
ls2=[]
for i in n:
    if i.isdigit():
        ls2.append(i)
        if len(ls2)>=len(ls):
            ls=ls2
    else:
        ls2=[]
if len(ls)==0:
    print('No digits')
else:
    print(''.join(ls))
