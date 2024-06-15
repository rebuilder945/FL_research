name = input().split(",")
grade = eval(input())
result = []
for i in range(len(name)):
    result1 = [name[i],grade[i]]
    result.append(result1)
print(result)

