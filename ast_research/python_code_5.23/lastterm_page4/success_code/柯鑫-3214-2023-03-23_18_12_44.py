list1=eval(input())
a=0
for x in list1:
    if x==0:
        a+=1
    
while a>0:
    list1.remove(0)
    list1.append(0)
    a-=1
print(list1)

