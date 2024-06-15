str1=input()
name=[str(n)for n in str1.split(",")]
grade=eval(input())
a=len(name)
b=0
lst1=[]
while a>0:
    lst2=[]
    lst2.append(name[b])
    lst2.append(grade[b])
    lst1.append(lst2)
    a-=1
    b+=1
print(lst1)

