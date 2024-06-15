n = eval(input())
d = []
if type(n)==int and n>1:
    for i in range(2,n):
        for t in range(2,i):
            if i%t == 0:
                break
        else:
            b = list(str(i))[::-1]
            c = "".join('%s' %i for i in b)
            e = eval(c)
            if i == e:
                d.append(i)
    f = " ".join('%s'%i for i in d)
    print(f)
else:
    print("illigal input")
