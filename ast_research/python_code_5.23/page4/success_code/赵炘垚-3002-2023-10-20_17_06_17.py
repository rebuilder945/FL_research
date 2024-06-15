m=eval(input())
if sum(m)%len(m)==0:
    print('%d'%(sum(m)%len(m)))
else:
    print(f'{sum(m)/len(m):.2f}')
