numbers=list(input())
for i in numbers:
    if i=='#':
        numbers.remove('#')
print(len(numbers),sum(numbers))
