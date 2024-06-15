# a=eval(input())
# a=str(a)
# a=list(a)
# b=[]
# for i in a:
#     i=(int(i)+5)%10
#     b.append(i)
# if len(b)==2:
#     b[0],b[-1]=b[-1],b[0]
# else:
#     b[0],b[-1]=b[-1],b[0]
#     b[1],b[-2]=b[-2],b[1]
# print(''.join(str(i) for i in b))
h=eval(input())
n=eval(input())
c=[]
if n==1:
    print('%.2f'%(h))
else:
    s=h
    for i in range(n):
        s=2*h*0.5**(i+1)
        c.append(s)
    a=sum(c)+h
    print("%.2f"%a)
        
    










