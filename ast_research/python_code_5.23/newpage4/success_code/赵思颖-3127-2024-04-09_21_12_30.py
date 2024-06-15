lists1=[]
a=int(input())
b=a+1
for i in range(1,b):
    lists1.append(i)
lists2=[x+1 for x in lists1]
# print(lists2)    
c=lists1.pop(0)
# print(c)
del lists2[-1]
lists2.append(c)
print(lists2)
