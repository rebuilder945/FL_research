names = input().split(',')
chengji = list(map(int,input().split(',')))
zuhe = list(zip(names,chengji))
result1 = sorted(zuhe,key = lambda x:x[1])
result2 = [list(x) for x in result1]
print(result2)
