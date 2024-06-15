a=input()
m=''
x=''
for i in a:
    if eval(i) in[0,1,2,3,4,5,6,7,8,9]:
        m+=i
        if len(m) > len(x):
            x=m
    else:
        m=''
if not m:
    print(x)
else:
    print('No digits')
