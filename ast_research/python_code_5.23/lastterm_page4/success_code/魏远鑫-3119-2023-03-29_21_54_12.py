list=eval(input())
result=[]
for i in range(len(list)):
    if list[i:].count(list[i])==1:
        result.append(list[i])
print(result)
