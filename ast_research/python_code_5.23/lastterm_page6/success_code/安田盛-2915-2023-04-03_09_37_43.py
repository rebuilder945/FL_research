a=eval(input())
c=[]
if a<100 or a>999:
    print('none')
else:
    for i in range(100,a+1):
        b=str(i)
        if int(b[0])**2+int(b[1])**2==int(b[2])**2:
            c.append(b)
            print(b)
if c==[]:
    print('none')
        
