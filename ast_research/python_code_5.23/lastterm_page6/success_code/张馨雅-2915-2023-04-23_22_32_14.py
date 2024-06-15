def shuxian(n):
    for i in range(100,n+1):
        s=str(i)
        if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
            print(i,end='\n')
number = int(input())
if shuxian(number) is True:
    print(shuxian(number))
else:
    print('none')
