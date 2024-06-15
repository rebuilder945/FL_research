n=eval(input())
numbers=[x for x in range(1,n+1)]
a=numbers.pop(0)
numbers.append(a)
print(numbers)
