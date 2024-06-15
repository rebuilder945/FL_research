i = 0
scores=[]
u,v,x,y = input().split(" ")
while i < 3:
    di=(("name",u),("english",int(v)),("python",int(x)),("math",int(y)))
    di = dict(di)
    scores.append(di)
    i=i+1
for i in scores:
    i["avg"]=round((i["english"]+i["python"]+i["math"])/3,2)
scores.sort(key=lambda x:x['avg'],reverse=True)
print(scores)
