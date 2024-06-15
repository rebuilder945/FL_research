n=eval(input())
lst1=[]
if n>100:
    for i in range(n):
        if int(i[0])**3+int(i[1])**3+int(i[2])**3==n:
            lst1.append(i)
        else:
            pass
else:
    print('none')

    
