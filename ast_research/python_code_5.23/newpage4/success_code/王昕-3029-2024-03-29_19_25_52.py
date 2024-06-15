name=list(eval(input()))
scores=eval(input())
x=[]
z=[]
#将名字和成绩绑定在同一个列表里面
for i in range(len(name)):
    z.append(name[i])
    z.append(scores[i])
    x.append(z)
    z=[]
print(x)
