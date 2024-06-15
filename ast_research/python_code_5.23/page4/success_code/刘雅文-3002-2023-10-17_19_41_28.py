a=eval(input())
b=sum(a)
if b%len(a)==0:
    c=b/len(a)
    print('%d'%(c))
else:
    c=b/len(a)
    print('%.2f'%(c))
