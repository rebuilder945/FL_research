def work(a) :
    lst1=[0]
    lst2=[1]
    b=1
    c=0
    while c<a:
        lst2.append(b)
        b=b*(c+2)
        c+=1
        lst1.append(c)
    dic=dict(zip(lst1,lst2))
    return dic
	

a = int(input())
ans = work(a)
print(ans)

