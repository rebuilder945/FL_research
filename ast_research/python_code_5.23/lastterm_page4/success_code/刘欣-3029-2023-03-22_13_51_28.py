names = input().split(",")
scores = eval(input())
result=[[name, scores[index]] for index, name in enumerate(names)]
print(result)
