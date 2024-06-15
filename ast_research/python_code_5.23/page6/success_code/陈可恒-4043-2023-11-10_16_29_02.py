s = ''.join(eval(input()))
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in s:
        n = s.count(i)
        print(i,n)


