n,m=input().split()
a=[]
b=[]
c=''
if int(m)-int(n)==3 and int(n)<int(m) and int(n)>=0:
    for i in range(int(n),int(m)):
        a.append(i)
    for x in a:
        for y in a:
            for z in a:
                if x!=y and y!=z and z!=x and x!=0:
                    sum=str(x)+str(y)+str(z)
                    b.append(sum)
    for i in b:
        c=c+i+' '
    print(c)
else:
    print('illegal input')
                    
