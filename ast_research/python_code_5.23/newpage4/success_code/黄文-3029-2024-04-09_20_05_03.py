from unittest import result


names=input().split(',')
scores=eval(input())
combine=zip(names,scores)
result_list=(list(combine))
print(result_list)

