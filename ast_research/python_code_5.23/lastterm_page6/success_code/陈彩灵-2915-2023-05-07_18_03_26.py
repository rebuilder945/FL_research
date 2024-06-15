def shuixianhua(n):
    if n<=100:
        print('none')
    elif n<=999:
        for i in range(100,n+1):
            i=str(i)
            if int(i[0])**3+int(i[1])**3+int(i[2])**3==int(i):
                print(i)
    else:
        for i in range(100,1000):
            i=str(i)
            if int(i[0])**3+int(i[1])**3+int(i[2])**3==int(i):
                print(i)
n=eval(input())
shuixianhua(n)



