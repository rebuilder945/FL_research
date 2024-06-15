str1=eval(input())
n,m=eval(input())
str2=str1.split()
a=str2[n]
b=str2[m]
str2[m]=a
str2[n]=b
print(str2)

