a=eval(input())
lst=[]
for i in range(1,a+1):
    lst.append(i)
b=lst[0]
lst.pop(0)
lst.append(b)
print(lst)



