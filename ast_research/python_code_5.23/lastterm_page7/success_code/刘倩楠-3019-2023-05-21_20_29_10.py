i=0
scores=[]
while i<3:
    u,v,x,y=input().split(" ")
    di=(("name",u),("english",v),("python",x),("math",y))
    di=dict(di)
    scores.append(di)
    i=i+1
for i in scores:
    i["avg"]=round((i["english"]+i["python"]+i["math"])/3,2)
def key(x):
    x['avg']
    return key(x)
scores.sort(key,reverse=True)
print(scores)
