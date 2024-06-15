list1=eval(input())
numbers=[]
for i in list1:
    if i not in numbers:
        numbers.append(i)
print(numbers)
