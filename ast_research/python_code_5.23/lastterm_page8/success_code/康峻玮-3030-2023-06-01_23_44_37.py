name= input().split(',')  
score= list(eval(input())) 
r = [[score[i],name[i]] for i in range(len(name))]
r =dict(r)
score.sort()
ls=[]
for i in range(len(score)):
    ls.append([r[score[i]],score[i]])
print(ls)
