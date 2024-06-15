digits = eval(input())
max_number = int(''.join(map(str, sorted(digits, reverse=True))))
print(max_number)

