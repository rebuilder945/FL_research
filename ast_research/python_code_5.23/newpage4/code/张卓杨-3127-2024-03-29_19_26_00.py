import numbers
n = eval(input())
numbers = [x for x in range(1,n+1)]
for i in range(1)：   
    num = numbers.pop(0)
    numbers.append(num)
print(numbers)

