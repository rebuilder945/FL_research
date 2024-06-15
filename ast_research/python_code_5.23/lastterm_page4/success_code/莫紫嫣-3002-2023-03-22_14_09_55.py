a=eval(input([1,2,3,4,5]))
b=sum(a)/len(a)
if b%1==0:
    print(int(b))
else:
    print('%.2f'%(b))
