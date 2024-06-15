i = 0
scores=[]
while i < 3:
    di=(("name",u),("english",int(v)),("python",int(x)),("math",int(y)))
    di = dict(di)
    scores.append(di)
    i=i+1
u,v,x,y = input().split(" ")
for i in scores:
    i["avg"]=round((i["english"]+i["python"]+i["math"])/3,2)
scores.sort(key=lambda x:x['avg'],reverse=True)
print(scores)
