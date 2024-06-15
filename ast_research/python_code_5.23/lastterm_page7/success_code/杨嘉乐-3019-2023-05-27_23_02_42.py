l=list(input().split(" "))
ll=["name","english","python","math"]
dic=dict(zip(ll,l))
dic["avg"]=sum([x for x in dic.values() if type(x)==int])/3
ss=[x for x in dic.values() if type(x)==int].sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(dic["name"],ss[0],ss[1],ss[2],dic["avg"]))
