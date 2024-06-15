lst=eval(input())
lst2=[]
b=""
while len(lst)>=1:
    a=max(lst)
    lst.remove(a)
    lst2.append(a)
# for i in range(len(lst2)):
#     lst2[i]=str(lst2[i])
str1=''.join(lst2)
print(int(str1))
