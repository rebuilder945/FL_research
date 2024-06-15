names = input("输入姓名：").split(',')
scores = input("输入成绩：").strip('[]').split(',')
scores = [int(score) for score in scores]
name_score = [[names[i],scores[i]] for i in range(len(names))]
print(name_score)
