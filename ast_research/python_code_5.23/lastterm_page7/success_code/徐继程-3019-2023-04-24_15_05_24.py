list=input().split()

a=int(list[1])
b=int(list[2])
c=int(list[3])
ave=(a+b+c)/3
if b>a:
    a,b=b,a
if c>a:
    a,c=c,a
if c>b:
    b,c=c,b
    
print('%s %.2f %.2f %.2f %.2f'%(list[0],a,b,c,ave))



