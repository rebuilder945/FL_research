names = input().split(',') 
scores = list(map(int, input().split(','))) 
pairs = list(zip (names, scores))
sorted_pairs = sorted(pairs, key=lambda x:x[1])
result = [[name, score] for name, score in sorted pairs] 
print(result)
