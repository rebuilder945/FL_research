a=input()
ls1=[]
ls2=[]
for x in a:
    if x in '0123456789':
        ls1.append(x)
        if len(ls1)>=len(ls2):
            ls2=ls1
    else:
        ls1=[]
if len(ls2)==0:
    print('No digits')
else:
    print(''.join(ls2))
