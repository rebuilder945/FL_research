def shuxian(n):
    for i in range(100,n):
        s=str(i)
        if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
            return i
n=eval(input())
print(shuxian(n),end='\n')
if shuxian(n)==False:
    print('none')
