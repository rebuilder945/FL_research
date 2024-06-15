ls=input().split()
dic={}
dic['name']=ls[0]
dic['english']=float(ls[1])
dic['python']=float(ls[2])
dic['math']=float(ls[3])
dic['avg']=(dic['math']+dic['english']+dic['python'])/3
ls2=list(map(float,ls[1:]))
ls2.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(ls[0],ls2[0],ls2[1],ls2[2],dic['avg']))
