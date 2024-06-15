s=''.join(eval(input()))
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in s:
        num=s.count(i)
        tem=i+','+str(num)
        print('%s'%tem)

        
