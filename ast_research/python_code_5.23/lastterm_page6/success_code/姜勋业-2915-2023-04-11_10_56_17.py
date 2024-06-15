n=eval(input())
if n<100:
    print('none')
else:
    for i in range(100,n+1):
        k=str(i)
        a,b,c=k[0],k[1],k[2]
        if i==int(a)**3+int(b)**3+int(c)**3:
            print(i)
