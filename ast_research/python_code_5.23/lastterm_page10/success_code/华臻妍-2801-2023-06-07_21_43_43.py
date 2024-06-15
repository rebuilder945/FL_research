s=input()
s1="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
#score是一个列表，初始值为0，表示密码一开始指标均为0
score=[0,0,0,0,0]
#当长度大于8时。表示第一次指标满足score[0]=1
if len(s)>=8:
    score[0]=1
for i in s:
    if i.islower():
        score[1]=1
    if i.isupper():
        score[2]=1
    if i.isdigit():
        score[3]=1
    if i in s1:
        score[4]=1
print(sum(score))
