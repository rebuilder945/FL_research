tep = input()
score = list(eval(input()))
name = tep.split(",")
for i in range(len(name)):
    ls=[]
    ls.append(name[i])
    ls.append(score[i])
    print(ls)
