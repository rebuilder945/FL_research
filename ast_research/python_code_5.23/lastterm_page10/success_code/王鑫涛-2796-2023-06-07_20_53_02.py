a=input()
m=0
x=0
for i in a:
    if eval(i) in[0,1,2,3,4,5,6,7,8,9]:
        m+=1
        if m > x:
            x=m
    else:
        m=0
if x!=0:
    print(x)
else:
    print('No digits')
