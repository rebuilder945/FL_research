a=eval(input())
a.sort(reverse=True)
if max(a)!=0:
    print(*a,sep='')
else:
    print('0')
