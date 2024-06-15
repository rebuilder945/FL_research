mingzi  =  eval(input())
jiji  =  eval(input())
zong  =  []
for i in range(min(len(mingzi), len(jiji))):
    zong.append([mingzi[i],jiji[i]])
print(zong)
