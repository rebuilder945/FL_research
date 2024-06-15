x=input().split( )
n1=eval(x[0])
n2=eval(x[1])
lis=[]
if n2-n1>=3 and type(n1)==int and type(n2)==int and n2>n1>=0:
    for x in range(n1,n2):
        for y in range(n1,n2):
            for z in range(n1,n2):
                if  x==y or x==z or z==y:
                    1    
                elif x==0:
                    1
                else:
                    num=str(x)+str(y)+str(z)
                    lis.append(num)
    for n in lis:
        print(int(n),end=' ')
else:
    print("illegal input")
