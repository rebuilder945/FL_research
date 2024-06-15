s=''.join(eval(input()))
for x in 'abcdefghijklmnopqrstuvwxzy':
    if x in s:
        num=s.count(x)
        tmp=x+','+str(num)
        print(tmp)
