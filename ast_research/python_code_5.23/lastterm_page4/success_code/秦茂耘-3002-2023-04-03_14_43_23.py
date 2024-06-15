A=eval(input())
a=sum(A)/len(A)
if type(a) is int:
    print('%s'%(a))
if type(a) is float:
    print('{:.2f}'.format(a))

