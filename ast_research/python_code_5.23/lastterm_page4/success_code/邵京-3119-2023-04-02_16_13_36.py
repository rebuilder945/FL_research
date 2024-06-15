list1=eval(input())
numbers=[]
for i in range(0,len(list1)):
    if list1.count(list[i])==1:
        numbers.append(list[i])
print(numbers)
