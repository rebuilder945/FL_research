a=eval(input())
list=[]
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            b=z**3+y**3+x**3
            c=100*x+10*y+z
            if b==c:
                list.append(c)
for i in list:
    if i<=a:
        print(i)
    elif list[0]>a:
        print('none')
        

