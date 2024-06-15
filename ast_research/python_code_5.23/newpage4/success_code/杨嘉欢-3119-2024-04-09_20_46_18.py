input=eval(input())
seen=set()
result=[]
for x in input:
    if x not in seen:
        seen.add(x)
        result.append(x)
    else:
        result.remove(x)
        result.append(x)
print(result)
