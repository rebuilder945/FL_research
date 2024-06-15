lst1=eval(input())
lst2=eval(input())
a=len(lst1)
jishu=0
lst3=[]
lst4=[]
while a>0:
    lst4=[]
    lst4.append(lst1[jishu])
    lst4.append(lst2[jishu])
    lst3.append(tuple(lst4))
    a-=1
    jishu+=1
print(lst3)
