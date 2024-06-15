info = input().split()
stu = {}
stu['name'] = info[0]
stu['english'] = info[1]
stu['python'] = info[2]
stu['math'] = info[3]
stu['avg'] = (stu['math']+stu['english']+stu['python'])/3
score = []
score.append(stu['english'])
score.append(stu['python'])
score.append(stu['math'])
score.sort(reverse=True)
print(stu['name'],end='')
for i in range(len(score)):
    print("%.2f"%(score[i]),end='')
print("%.2f"%stu['avg'])
