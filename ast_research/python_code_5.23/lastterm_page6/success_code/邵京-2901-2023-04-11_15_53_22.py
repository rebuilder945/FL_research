numbers=list(eval(input(),sep=''))
for i in numbers:
    if i=='!#':
        numbers.remove('!#')
print(len(numbers),sum(numbers))
