s = ''.join(eval(input()))
for x in 'abcdefghijklmnopqrstuvwxyz':
    if x in s:
        a = s.count(x)
        d = x+','+str(a)
        print(d)
