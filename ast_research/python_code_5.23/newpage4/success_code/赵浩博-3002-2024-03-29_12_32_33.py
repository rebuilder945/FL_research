a=eval(input())
avg=sum(a)/len(a)
if sum(a)%len(a)==0:
    print(int(avg))
else:
    print('%.2f'%(avg))
