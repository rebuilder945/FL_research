a=eval(input())
n=[]
if a<=1 or int(a)!=a:
    print('illegal input')
else:
    a=int(a)
    for i in range(2,a+1):
        b=str(i)[::-1]
        if i==b:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                n.append(i)
for x in n:
    print('%d'%x,end='')
