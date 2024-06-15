str1=input()
list1=[str(n) for n in str1.split(',')]
list2=eval(input())
l=len(list1)
a=0
list3=[]
while l>0:
    x1=[]
    x1.append(list1[a])
    x1.append(list2[a])
    list3.append(x1)
    a+=1
    l-=1
print(list3)
