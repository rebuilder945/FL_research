ls1=[]
ls2=[]
ls3=[]
ls4=[]
p=input()
if len(p)>=8:
    i=1
else:
    i=0
for x in p:
    if x in '0123456789':
        ls1.append(x)
    elif x in 'abcdefghijklmnopqrstuvwxyz':
        ls2.append(x)
    elif x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        ls3.append(x)
    elif x in '~!@#$%^&*()_=-/,.?<>;:[]{}\|':
        ls4.append(x)
if len(ls1)!=0:
    i=i+1
if len(ls2)!=0:
    i=i+1
if len(ls3)!=0:
    i=i+1
if len(ls4)!=0:
    i=i+1
print(i)

