l=list(map(str,input().split(" ")))
ll=["name","english","python","math"]
dic=dict(zip(ll,l))
dic.setdefault("avg",sum([int(x) for x in l if x.isdigit()])/3)
ss=sorted([int(x) for x in l if x.isdigit()],reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(dic["name"],ss[0],ss[1],ss[2],dic["avg"]))
