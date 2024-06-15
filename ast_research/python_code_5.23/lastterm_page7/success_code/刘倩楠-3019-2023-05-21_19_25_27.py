u,v,x,y=input().split(" ")
di=(("name",u),("english",v),("python",x),("math",y))
di=dict(di)
avg=(eval(v)+eval(x)+eval(y))/3
di["avg"]=avg
di=list(di)
di.sort[1:]()
di=dict(di)
print(di.values())
