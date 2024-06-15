l=list(input().split(" "))
ll=["name","english","python","math"]
dic=zip(ll,l)
dic["avg"]=sum([x for x in dic.values() if type(x)==int])/3
ss=[x for x in dic.values() if type(x)==int].sort(True)
print("%s %.2f %.2f %.2f %.2f"%(dic["name"],ss[1],ss[2],ss[3],dic["avg"]))
