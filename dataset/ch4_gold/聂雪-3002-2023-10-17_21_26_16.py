ls=eval(input())
a=sum(ls)/len(ls)
c=sum(ls)%len(ls)
if c==0:
    print(int(a))
else:
    print('%.2f'%a)
