ls=eval(input())
lssum=sum(ls)
n=sum(ls)/len(ls)
if sum(ls)%len(ls)==0:
    print(int(n))
else:
    print('%.2f'%n)
