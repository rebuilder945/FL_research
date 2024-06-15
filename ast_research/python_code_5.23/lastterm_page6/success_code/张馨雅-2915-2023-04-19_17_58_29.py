def shuxian(n):
    for i in range(100,n):
        s=str(i)
        if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
            print(i,end='\n')
flag = 0
number = int(input())
if shuxian(number):
    if False:
        print('none')
