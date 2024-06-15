a=input()
lst1=[]
for i in range(len(a)):
    lst1.append(a[i])
for i in range(len(lst1)):
    lst1[i]=(int(lst1[i])+5)%10 
lst1.reverse()
for i in range(len(lst1)):
    lst1[i]=str(lst1[i])
str1=''.join(lst1)
print(str1)


