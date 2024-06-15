a=eval(input())
c=[]
if a<100 or a>999:
    print('none')
else:
    for i in range(100,a+1):
        b=str(i)
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==int(b):
            c.append(b)
            print(int(b))
    if c==[]:
        print('none')
        
