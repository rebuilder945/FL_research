names=input().split(',')
marks=input().split(',')
result=[]
for x in range(len(names)):
    result.append([names[x],marks[x]])
result.sort(key=lambda x: x[1])
print(result)
