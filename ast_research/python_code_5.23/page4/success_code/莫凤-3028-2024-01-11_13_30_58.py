a,b,c=eval(input())
list1=[]
list1.append(a)
for x in range(b-1):
    a+=c
    list1.append(a)
print(list1)
