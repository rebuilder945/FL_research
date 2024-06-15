tep = input()
score = list(eval(input()))
s = []
name = tep.split(",")
for i in range(len(name)):
    ls=[]
    ls.append(name[i])
    ls.append(score[i])
    s.append(ls)
print(s)
