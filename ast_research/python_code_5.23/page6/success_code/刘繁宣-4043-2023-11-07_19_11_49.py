s=''.join(eval(input()))
for x in 'abcdefghijklmnopqrstuvwxyz':
    if x in s:
        n=s.count(x)
        if n >0:
            print(x+','+str(n))
