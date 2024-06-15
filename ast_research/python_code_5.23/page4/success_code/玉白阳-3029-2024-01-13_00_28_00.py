name=list(input().split(","))
score=eval(input())
list=[[name[i],score[i]]for i in range(len(name))]
print(list)
