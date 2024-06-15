a = eval(input())

result = []
for i, x in enumerate(a):
    if x not in result:
        result.append(x)
    else:
        a.pop(i)

print(result)
