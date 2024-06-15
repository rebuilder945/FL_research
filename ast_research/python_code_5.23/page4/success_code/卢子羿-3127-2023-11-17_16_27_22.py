n=eval(input())
list1=[]
m=eval("1")
for x in range(2,n+1):
    if x not in list1:
        list1.append(x)
        list1.sort(reverse=False)
list1.append(m)
print(list1)

