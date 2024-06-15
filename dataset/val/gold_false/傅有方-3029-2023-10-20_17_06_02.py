names=['tom','jack','jone','mike']
scores=[88,89,34,90]
result=list(zip(names,scores))
sorted_result=sorted(result, key=lambda x:x[1])
print(sorted_result)
