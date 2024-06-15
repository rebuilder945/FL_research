u,v,x,y=input().split(" ")
di=(("name",u),("english",v),("python",x),("math",y))
di=dict(di)
avg=(eval(v)+eval(x)+eval(y))/3
d["avg"]=avg
di.sort()
print(di.values())
