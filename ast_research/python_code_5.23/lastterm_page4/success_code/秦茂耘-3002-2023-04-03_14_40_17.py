A=eval(input())
a=sum(A)/len(A)
if sum(A) % len(A) == 0:
    print('%s'%(a))
else:
    print('{:.2f}'.format(a))

