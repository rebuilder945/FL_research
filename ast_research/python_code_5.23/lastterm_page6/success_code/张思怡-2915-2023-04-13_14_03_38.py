def narc(n):
    a=n%10
    b=n//10%10
    c=n//100
    if a**3+b**3+c**3==n:
        return True
    else:
        return False
n=int(input())
str1=[]
f=0
if f==0:
    for i in range(100,n):
        if narc(i):
            f=1
            str1.append(i)
    for x in range(len(str1)):
        print(str1[x])
elif f ==1:
    print("none")
