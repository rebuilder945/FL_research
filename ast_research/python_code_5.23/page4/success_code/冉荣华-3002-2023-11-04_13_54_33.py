X=eval(input())
if sum(X)%len(X)==0:
    print('%d'%(sum(X)/len(X)))
else:
    print(f'{sum(X)/len(X):.2f}')
