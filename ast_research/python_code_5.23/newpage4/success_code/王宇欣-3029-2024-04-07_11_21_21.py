a = str(input())
b = eval(input())
result =[]
for i in range(len(a)):
    list = [a(i),b(i)]
    result.append(list)
print(result)
