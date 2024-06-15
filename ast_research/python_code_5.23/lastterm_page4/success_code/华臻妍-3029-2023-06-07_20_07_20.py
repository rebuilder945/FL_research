name = list(input().split(','))
score = eval(input())
name_score=[]
for i in range(0,len(name)):#从0开始到len长的数
    a=name[i]
    b=score[i]
    temp = [a,b]
    name_score.append(temp)
print(name_score)
