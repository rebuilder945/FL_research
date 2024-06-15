ls=input().split(",")
a,b=eval(input())
str1=ls[a]
str2=ls[b]
ls[a]=str2
ls[b]=str1
print(ls)
