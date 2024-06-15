a=input()
m=''
x=0
for i in a:
    if eval(i) in[0,1,2,3,4,5,6,7,8,9]:
        m+=i
        if len(m) > x:
            x=len(m)
    else:
        m=0
if m!=0:
    print(x)
else:
    print('No digits')
