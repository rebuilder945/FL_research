def lstdelete(m,n,t):
    if n not in m or t not in m:
        print("error")
    else:
        a = m.index(n)
        b = m.index(t)
        c = m[a:b]
        d = []
        for i in m:
            if i not in c:
                d.append(i)
                print(d)
            else:
                True
    return 

x = eval(input())
y,z = eval(input())
print(lstdelete(x,y,z))
    

    












