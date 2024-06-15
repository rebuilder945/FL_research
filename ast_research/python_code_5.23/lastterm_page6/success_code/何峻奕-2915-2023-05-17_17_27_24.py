def Narc(n):
    a=n%10
    b=n//10%10
    c=n//100
    if a**3+b**3+c**3==n:
        return True
    else:
        return False
c=eval(input())
str1=""
for i in range(100,c):
    if Narc(i):
        str1=str1+str(i)+","
a=str1.split(',')
if a==[]:
    print("none")
for i in a:
    print(i)
        
