n=int(input())
lst1=[]
if n>100 and n<1000:
    for i in range(100,1000):
        if int(str(i)[0])**3*100+int(str(i)[1])**3*10+int(str(i)[2])**3==n:
            lst1.append(i)
        else:
            pass
    print(lst1)
else:
    print('none')

    
