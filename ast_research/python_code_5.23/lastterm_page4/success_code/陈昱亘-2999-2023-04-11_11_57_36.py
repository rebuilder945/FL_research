string=input()
str1=input()
lst2=str1.split(' ')
n=int(lst2[0])
m=int(lst2[-1])
lst3=string.split(' ')
lst4=[x for x in lst3]
lst3[n]=lst4[m]
lst3[m]=lst4[n]
print(lst3)
