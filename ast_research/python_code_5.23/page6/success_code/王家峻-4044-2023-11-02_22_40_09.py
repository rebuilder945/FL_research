n=eval(input())
str=""
for i in range(1,n):
    a=i
    b=0
    for j in range(3):
        n1=a%10
        b=b+n1**3
        a=a//10
    if b==i:
        str1=str1 +str(i)+","
print(str[:-1])

