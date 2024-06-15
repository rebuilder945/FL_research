u,v,x,y=input().split(" ")
di=(("name",u),("english",v),("python",x),("math",y))
di=dict(di)
avg=(v+x+y)/3
d["avg"]=avg
di.sort()
print(di.values())
