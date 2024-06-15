a,b=input().split()
s=[]
if type(eval(a))!=int or type(eval(b))!=int or a>b:
    print('illegal input')
else:
    a=int(a)
    b=int(b)
    for x in range(a,b):
        for y in range(a,b):
            for z in range(a,b):
                if x!=y!=z and x!=0:
                    c=x*100+y*10+z
                    c=str(c)
                    s.append(c)
                    print(c,end=" ")
if len(s)==0:
    print('illegal input')


