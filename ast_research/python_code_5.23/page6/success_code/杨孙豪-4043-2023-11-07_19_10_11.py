s=''.join(eval(input()))
for x in 'abcdefghijklmnopqrstuvwxyz':
    if x in s:
        n=s.count(x)
        t=x+','+str(n)
        print(t)
