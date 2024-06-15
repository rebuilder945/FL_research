b=''.join(eval(input()))
for i in"abcdefghijklmnopqrstuvwxyz":
    if i in b:
        num=b.count(i)
        a=i+','+str(num)
        print(a)


