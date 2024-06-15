a=input()
a +=' '
s=''
b=[]
c=' '
for i in range(len(a)-1):
    if '0'<=a[i]<= '9':
        s+=a[i]
    if len(s)>0 and (a[i+1]<'0' or a[i+1]>'9'):
        b.append(s)
        s=''
if len(b)==0:
    print('No digits')
else:
    for i in b:
        if len(i)>=len(c):
            c=i
    print(c)
