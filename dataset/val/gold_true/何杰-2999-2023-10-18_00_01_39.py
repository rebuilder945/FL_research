str1=input().split()
n=input().split()
a=int(n[0])
b=int(n[1])
str1[a],str1[b]=str1[b],str1[a]
print(str1)
