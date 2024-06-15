names = input().split(",")
scores = eval(input())
result=[[name, scores[index]] for index, name in enumerate(names)]
result.sort(key=lambda x:x[-1])
print(result)
