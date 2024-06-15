def ss(n):
    b=str(n)
    if int(b[0])**3+int(b[1])**3+int(b[2])**3==n:
        return True
    else:
        return False
n=int(input())
for x in range(100,n+1):
    if ss(x):
        print(x)
    else:
        print('none')
        break
