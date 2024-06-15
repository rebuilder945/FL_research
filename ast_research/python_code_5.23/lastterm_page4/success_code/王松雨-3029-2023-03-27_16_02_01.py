names=input().split(',')
scores=eval(input())
lb=[]
for i in range(len(names)):
 lb.append(list(names[i],scores[i]))
print(lb)
