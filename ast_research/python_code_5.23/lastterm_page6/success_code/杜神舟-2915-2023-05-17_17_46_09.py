def ss(n):
    b=str(n)
    if int(b[0])**3+int(b[1])**3+int(b[2])**3==int(n):
        return True
    else:
        return False
n=int(input())
i=0
for x in range(100,n+1):
    if ss(int(x)):
        i=1
        print(x)
if i==0:
    print('none')
