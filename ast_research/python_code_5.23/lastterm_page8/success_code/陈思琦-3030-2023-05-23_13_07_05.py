names=list(input().split(','))
grades=list(eval(input()))
total=[[x,y]for x in names  for y in grades if names.index(x)==grades.index(y)]
total.sort(key=lambda total:total[1],reverse=False)
print(total)

