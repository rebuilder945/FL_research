names = input().split(",")
scores = input().split(",")
result = [ ]
for name,score in zip(names,scores):
    result.append([name,score])
result.sort(key=lambda x:x[1])
print(result)
     
    
