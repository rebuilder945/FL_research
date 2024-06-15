str1=input()
len1=len(str1)
str2=input()
l=len(str2)
s=''
for i in range(len1-l+1):
    if str1[i:i+l]!=str2:
        s+=str1[i:l+i]
        i=i+l-1
print(s)


