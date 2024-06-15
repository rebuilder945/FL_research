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
if c>=1000:
    c=1000
for i in range(100,c):
    if Narc(i):
        str1=str1+str(i)+","
if str1=="":
    print("none")
a=str1.split(',')
for i in a:
    print(i)
        
