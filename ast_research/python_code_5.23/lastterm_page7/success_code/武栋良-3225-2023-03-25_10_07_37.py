def work(a) :
    lst = [(0,1)]
    if a==0:
        lst = lst
    else:
        for x in range(1,a+1):
            s = 1
            for n in range(1,x+1):
                s = s*n
            b = (x,s)
            lst.append(b)
    dit = dict(lst)
    return dit
	

a = int(input())
ans = work(a)
print(ans)

