def shuxian(n):
    for i in range(100,n):
        s=str(i)
        if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
            print(i,end='\n')
flag = 0
number = int(input())
for i in range(100,number+1):
    if shuxian(i):
        flag = 1
if flag == 0:
    print('none')
