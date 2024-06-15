L=eval(input())
list1=sorted(L)
list2=list1[::-1]
x=''
for i in list2:
    x=x+str(i)
print(x)

