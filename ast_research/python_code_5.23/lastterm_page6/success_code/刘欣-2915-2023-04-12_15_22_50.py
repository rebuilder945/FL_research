zhengshu=str(input())
str=""
for i in range(zhengshu):
    n=i
    s=0
    for j in range(len(zhengshu)):
        n1=n%10
        s=s+n1**3
        n=n//10
    if s==i:
        str1=str1+str(i)+","
print(str1[:-1])
