list1=eval(input())
list1.sort(reverse=True)
x=[i*10**index for index,i in enumerate(list1[::-1])]
y=sum(x)
print(y)

