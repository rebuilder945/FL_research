n,m=map(str,input().split(' '))
if int(n)+3<=int(m):
    lst1=[]
    lst2=range(int(n),int(m))
    for x in lst2:
        for y in lst2:
            for z in lst2:
                 if x!=y and x!=z and y!=z:
                     san1=str(x)+str(y)+str(z)
                     lst1.append(int(san1))
    print(*lst1,sep=" ")
else:
    print("illegal input")
            



