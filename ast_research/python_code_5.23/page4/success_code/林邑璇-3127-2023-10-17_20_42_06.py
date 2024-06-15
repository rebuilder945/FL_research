a=eval(input())
list=[]
for i in range(1,a+1):
    list.append(i)
list.append(list[0])
list.remove(list[0])
print(list)
