n=eval(input())
m=0
for i in list(range(100,n+1)):
    if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
        print(i)
        m=1
    else:
        pass
if m==0:
    print('none')

