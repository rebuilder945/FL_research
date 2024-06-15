a=''.join(eval(input()))
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in a:
        b=a.count(i)
        print('%s,%d'%(i,b))
