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
a=eval(input())
b=eval(input())
c=[]
if b==1:
    print('%.2f'%(a))
else:
    for i in range(1,b):
        d=2*a*0.5**i
        c.append(d)
    print('%.2f'%(a+sum(c)))


        
    










