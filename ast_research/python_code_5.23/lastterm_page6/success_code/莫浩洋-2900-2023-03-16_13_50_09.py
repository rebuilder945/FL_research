a=eval(input())             #注意remove不要与遍历操作同时针对同一个列表
b=[]
c=[]
d=list(range(2,a))
if a<=1 or a%1!=0:
    print("illegal input")
else :
    b.extend(d)
    for i in d:
        for x in range(2,i):
            if i%x==0:
                b.remove(i)
                break
    c.extend(b)
    for z in b:   
        for y in range(len(str(z))):
            if str(z)[y]!=str(z)[-y-1]:
                c.remove(z)
                break
    print(*c,sep=" ")
