def shui(n):
    lst =[]
    if n < 100:
        return 'none'
    else:
        for x in range(100,n+1):
            a = str(x)
            if eval(a[0])**3+eval(a[1])**3+eval(a[2])**3 == x:
                lst.append(x)
        if len(lst)==0:
            return 'none'
        else:
            s = ",".join(map(str,lst))
            return s
m = eval(input())
a = shui(m)
print(a)



    
