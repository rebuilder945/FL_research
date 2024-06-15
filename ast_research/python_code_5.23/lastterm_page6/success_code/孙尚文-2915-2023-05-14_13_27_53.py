def shuixianhuashu(n):
    gewei=n%10
    shiwei=n//10%10
    baiwei=n%100
    if n<100 or n>999:
        return False
    elif n==gewei**3+shiwei**3+baiwei**3:
        return True
    return False
a=eval(input())
b=0
for i in range(a):
    if shuixianhuashu(i):
        b+=1
        print(i)
if b==0:
    print("none")
        
    
