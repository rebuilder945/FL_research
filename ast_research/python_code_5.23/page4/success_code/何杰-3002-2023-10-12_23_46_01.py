n=eval(input())
x=sum(n)/len(n)
if x-int(x)==0:
    print(int(x))
elif x-int(x)!=0:
    print('%.2f'%x)
