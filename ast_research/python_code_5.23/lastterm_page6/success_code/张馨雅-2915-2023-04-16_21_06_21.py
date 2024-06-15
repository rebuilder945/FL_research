def shuxian(n):
    while n>=1:
        if n%10==(n%10)**3:
            n=n//10
            return True
        else:
            return False
n=eval(input())
m=0
for i in range(0,100):
    if shuxian(i):
        print(i,end='\n')
        m+=1
    if m==0:
        print('none')
