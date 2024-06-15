def jiami(shuru):
    b =  [int(x) for x in shuru]
    c = [(x+5)%10 for x in b]
    for i in range(len(c)//2):
        c[i],c[-i-1] = c[-i-1],c[i]
    d = "".join(str(x) for x in c)
    return d

e = input()
f = jiami(e)
print(f)
