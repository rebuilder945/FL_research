x = ''.join(eval(input()))
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in x:
        a = x.count(i)
        b = i+','+str(a)
        print(b)

