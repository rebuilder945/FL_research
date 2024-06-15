def shuixian(x):
    x=str(x)
    if len(x)==3:
        if int(x[0])**3+int(x[1])**3+int(x[2])**3==int(x):
            return True
        else:
            return False
n=eval(input())
a=0
for i in range(n+1):
    if shuixian(i):
        print(i)
    else:
        a+=1
if a==n+1:
    print('none')
