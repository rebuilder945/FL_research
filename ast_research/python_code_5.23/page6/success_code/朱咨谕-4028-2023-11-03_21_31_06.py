def su(n):
    a=0
    for i in range(1,n):
        if n%i==0 : a+=1
    if a==1 : return 1
    else : return 0

def hui(n):
    if str(n)[::]==str(n)[::-1] : return 1
    else : return 0
    
n=eval(input())
print(type(n))
if n<0 or type(n)!=int:
    print("illegal input")
else : 
    for i in range(n+1):
        if su(i) and hui(i) : print(i,end=' ')
       
