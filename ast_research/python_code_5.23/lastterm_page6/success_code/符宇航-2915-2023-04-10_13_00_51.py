n = eval(input())
if n<=100:
    print('none')
else:
    s=0
    qq=[]
    for i in range(100,n+1):
        i = str(i)
        for x in i:
            x = int(x)
            s+=x**3
        i=int(i)
        if s == i:
            print(s)
            qq.append(s)
    if len(qq)==0:
        print('none')
        

