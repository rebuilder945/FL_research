a,b,c,d=input().split()
e={}
e["name"]=a
e['english']=int(b)
e['python']=int(c)
e['math']=int(d)
e['avg']=(int(b)+int(c)+int(d))/3
print("%s %.2f %.2f %.2f %.2f"%(e["name"],e['english'],e['python'],e['math'],e['avg']))
