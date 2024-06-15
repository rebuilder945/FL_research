list0=input().split(',')
a=1
list1=[]
while a <= int(list0[1]):
    list1.append(int(list0[0]))
    list0[0]=int(list0[0])+int(list0[2])
    a+=1
print(list1)
