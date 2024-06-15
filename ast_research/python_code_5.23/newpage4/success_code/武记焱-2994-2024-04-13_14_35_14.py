list1=input().split(',')
n,m=eval(input())
x=len(list1)-1
y=-len(list1)
if n>x or n<y:
    print("error")
else:
    list2=[list1[n]]*m
    list3=list1+list2
list4=[]
for i in list3:
    i=int(i)
    list4.append(i)
print(list4)
