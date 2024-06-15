list=input().split(',')
list2=eval(input())
list3=[]
n=len(list2)
for i in range(0,n):
    i=[list[i],list2[i]]
    list3.append(i)
print(list3)
