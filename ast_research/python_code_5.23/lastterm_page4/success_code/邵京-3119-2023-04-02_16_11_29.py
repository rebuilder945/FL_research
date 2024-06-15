list1=eval(input())
numbers=[]
for i in list1:
    if list1.count(i)==1:
        numbers.append(i)
print(numbers)
