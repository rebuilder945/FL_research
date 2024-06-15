a=list(input())
a.reverse()
a.append('a')
c=''
d=''
for i in range(len(a)):
    if a[i] in ['0','1','2','3','4','5','6','7','8','9']:
        c+=a[i]
    else:
        if len(c)>len(d):
            d=c
        c=''
if d=='':
    print('No digits')
else:
    print(d[::-1])


