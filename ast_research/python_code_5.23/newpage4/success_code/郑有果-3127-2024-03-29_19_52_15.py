import numbers
n=eval(input())
numbers=[i for i in range(1,n+1)]
for a in range(1):
        numbers.remove(a)
        numbers.append(a)
print(numbers)
