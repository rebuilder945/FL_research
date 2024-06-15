ls=input().split()
dic={}
dic['name']=ls[0]
dic['english']=float(ls[1])
dic['python']=float(ls[2])
dic['math']=float(ls[3])
dic['avg']=(dic['math']+dic['english']+dic['python'])/3
ls2=ls[1:4].sort(reverse=True)
ls3=list(map(float,ls2))
print("%s %.2f %.2f %.2f %.2f"%(ls[0],ls3[0],ls3[1],ls3[2],dic['avg']))
