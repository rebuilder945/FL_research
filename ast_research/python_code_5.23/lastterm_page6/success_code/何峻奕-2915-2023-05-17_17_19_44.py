def Narc(n):
    a=n%10
    b=n//10%10
    c=n//100
    if a**3+b**3+c**3==n:
        return True
    else:
        return False
str1=" "
for i in range(100,1000):
    if Narc(i):
        str1=str1+str(i)+","
print(str1[:-1])
