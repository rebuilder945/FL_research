names = input().split(',')
chengji = list(map(int,input().split(',')))

pairs = list(zip(names,chengji))

result = sorted(pairs,key = lambds x:x[1])
result = [list(x) for x in result]

print(result)
