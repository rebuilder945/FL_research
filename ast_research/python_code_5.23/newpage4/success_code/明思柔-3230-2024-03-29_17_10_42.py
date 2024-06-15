numbers=list(eval(input()))
numbers.sort(reverse=True)
result=""
for number in numbers:
    result += str(number)
result=int(result)
print(result)
