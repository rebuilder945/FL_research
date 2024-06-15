ls=''.join(eval(input()))
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in ls:
        a=ls.count(x)
        b=a+","+str(a)
        print(b)

