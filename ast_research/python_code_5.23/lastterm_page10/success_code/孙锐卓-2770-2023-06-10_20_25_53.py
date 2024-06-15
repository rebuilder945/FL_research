m=input()
n=input()
m1=[x for x in m]
n1=[x for x in n]
a=[]
if len(m1)!=len(n1):
    print('False')
else:
    for i in m1:
        if i not in n1:
            a.append(i)
    if len(a)==0:
        print('True')
    else:
        print('False')


