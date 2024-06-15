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
if 1000>n>152:
    for i in range(100,n):
        if narc(i):
            str1.append(i)
    for x in range(len(str1)):
        print(str1[x])
else:
    print("none")
