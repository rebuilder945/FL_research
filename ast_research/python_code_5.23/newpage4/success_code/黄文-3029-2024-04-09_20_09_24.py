from unittest import result


names=input().split(',')
scores=eval(input())
combine=zip(names,scores)
result_list=(list(pair) for pair in combine)
print(result_list)

